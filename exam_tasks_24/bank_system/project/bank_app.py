from typing import List

from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:

    VALID_TYPE_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_TYPE_CLIENTS = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.loans: List = []
        self.clients: List = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_TYPE_LOANS:
            raise Exception("Invalid loan type!")
        new_loan = self.VALID_TYPE_LOANS[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_TYPE_CLIENTS:
            raise Exception("Invalid client type!")
        if len(self.clients) > self.capacity:
            return "Not enough bank capacity."
        new_client = self.VALID_TYPE_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        if loan_type not in self.VALID_TYPE_LOANS:
            raise Exception("Inappropriate loan type!")
        loan = next((l for l in self.clients if client_id == l.client_id))
        self.loans.remove(loan)



    def remove_client(self, client_id: str):
        pass

    def increase_loan_interest(self, loan_type: str):
        pass

    def increase_clients_interest(self, min_rate: float):
        pass

    def get_statistics(self):
        pass

    # def _get_loan(self, type_loan):
    #     loan = [c for c in self.loans if c.name == type_loan]
    #     return loan[0] if loan else None
