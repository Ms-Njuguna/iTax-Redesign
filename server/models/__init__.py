from extensions import db
from .audit import AuditLog
from .user import User
from .income import IncomeType, ReturnIncome  # <-- Moved this import up
from .tax_return import Return              # <-- Moved this import down
from .deduction import ReturnDeduction
from .payment import Payment