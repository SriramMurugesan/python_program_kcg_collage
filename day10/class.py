# Create abstract class Shape with method area()


class A(ABC):
    @abstractmethod
    def show(self):
        pass

class B(A):
    pass

obj = B()

# Add one normal method in abstract class

# Force subclass to define salary

# Print numbers from 1 to 3 using custom iterator

# All payment methods must follow same rules → use abstract class

# Scenario:

# Company has:

# FullTime employees
# Freelancers

# Salary calculation differs

# Design:

# Force all employees to implement calculate_salary()


# Scenario:

# App sends notifications via:

# Email
# SMS

# Design:

# Force all to implement send()

# Scenario:

# Every user must have role

# Design:

# Force property definition