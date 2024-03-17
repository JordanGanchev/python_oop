from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:

    VALID_TYPE_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_TYPE_CLIENTS = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_TYPE_LOANS:
            raise Exception("Invalid loan type!")
        new_loan = self.VALID_TYPE_LOANS[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."
        # create object with eval
        # if loan_type == "StudentLoan" or loan_type == "MortgageLoan":
        #     loan = eval(f"{loan_type}()")

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_TYPE_CLIENTS:
            raise Exception("Invalid client type!")
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."
        new_client = self.VALID_TYPE_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        # if loan_type not in self.VALID_TYPE_LOANS:
        #      raise Exception("Inappropriate loan type!")
        # loan = next((l for l in self.clients if client_id == l.client_id))
        # self.loans.remove(loan)
        client = [c for c in self.clients if c.client_id == client_id][0]
        if (loan_type == "StudentLoan" and client.__class__.__name__ == "Student") or (
            loan_type == "MortgageLoan" and client.__class__.__name__ == "Adult"
        ):
            loan = [l for l in self.loans if l.__class__.__name__ == loan_type][0]
            self.loans.remove(loan)
            client.loans.append(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."
        else:
            raise Exception("Inappropriate loan type!")


    def remove_client(self, client_id: str):
        try:
            client = [c for c in self.clients if c.client_id == client_id][0]
        except IndexError:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        counter = 0
        for l in self.loans:
            if l.__class__.__name__ == loan_type:
                l.increase_interest_rate()
                counter += 1
        return f"Successfully changed {counter} loans."

    def increase_clients_interest(self, min_rate: float):
        counter = 0
        for c in self.clients:
            if c.interest < min_rate:
                c.increase_clients_interest()
                counter += 1
        return f"Number of clients affected: {counter}."

    def get_statistics(self):
        total_clients_income = sum([c.income for c in self.clients])
        loans_count_granted_to_clients = sum([len(c.loans) for c in self.clients])
        granted_sum = sum([l.amount for c in self.clients for l in c.loans])
        not_granted_sum = sum(l.amount for l in self.loans)
        try:
            avg_client_interest_rate = sum([c.interest for c in self.clients])/len(self.clients)
        except ZeroDivisionError:
            avg_client_interest_rate = 0

        result = f"Active Clients: {len(self.clients)}\n"
        result += f"Total Income: {total_clients_income:.2f}\n"
        result += f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"
        result += f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n"
        result += f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
        return result



    # def _get_loan(self, type_loan):
    #     loan = [c for c in self.loans if c.name == type_loan]
    #     return loan[0] if loan else None
