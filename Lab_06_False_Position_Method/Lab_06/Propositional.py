class Proposition:
    def __init__(self, name, truth_value=None):
        self.name = name
        self.truth_value = truth_value

    def set_truth_value(self, truth_value):
        self.truth_value = truth_value

    def evaluate(self):
        return self.truth_value


class BinaryOperator:
    def __init__(self, left, right, name=None):
        self.left = left
        self.right = right
        self.name = name if name is not None else f"({left.name} {self.get_operator_symbol()} {right.name})"

    def get_operator_symbol(self):
        raise NotImplementedError("Subclasses must implement this method")

    def set_truth_value(self, truth_value):
        # You can choose how to handle setting the truth value for operators
        # For simplicity, let's ignore it for operators
        pass


class AndOperator(BinaryOperator):
    def evaluate(self):
        return self.left.evaluate() and self.right.evaluate()

    def get_operator_symbol(self):
        return "AND"


class OrOperator(BinaryOperator):
    def evaluate(self):
        return self.left.evaluate() or self.right.evaluate()

    def get_operator_symbol(self):
        return "OR"


class NotOperator:
    def __init__(self, operand):
        self.operand = operand

    def evaluate(self):
        return not self.operand.evaluate()

    @property
    def name(self):
        return f"NOT {self.operand.name}"

    def set_truth_value(self, truth_value):
        # Ignore setting truth value for NOT operator
        pass


class ImplicationOperator(BinaryOperator):
    def evaluate(self):
        return not self.left.evaluate() or self.right.evaluate()

    def get_operator_symbol(self):
        return "=>"


class BiconditionalOperator(BinaryOperator):
    def evaluate(self):
        return self.left.evaluate() == self.right.evaluate()

    def get_operator_symbol(self):
        return "<=>"


def generate_truth_table(propositions):
    num_props = len(propositions)
    header = [prop.name for prop in propositions]
    table = []

    for i in range(2 ** num_props):
        row = []
        for j in range(num_props):
            propositions[j].set_truth_value((i >> (num_props - 1 - j)) % 2 == 1)
            row.append(str(propositions[j].evaluate()))
        table.append(row)

    return header, table

def print_truth_table(header, table):
    col_widths = [max(len(cell) for cell in col) for col in zip(*table)]

    print("Truth Table:")
    for i, cell in enumerate(header):
        print(f"{cell:^{col_widths[i]}}", end=" | ")
    print()

    for row in table:
        for i, cell in enumerate(row):
            print(f"{cell:^{col_widths[i]}}", end=" | ")
        print()

# Example usage:

p = Proposition("P")
q = Proposition("Q")

p_and_q = AndOperator(p, q)
p_or_q = OrOperator(p, q)
not_p = NotOperator(p)
p_implies_q = ImplicationOperator(p, q)
p_iff_q = BiconditionalOperator(p, q)

propositions = [p, q, p_and_q, p_or_q, not_p, p_implies_q, p_iff_q]

header, table = generate_truth_table(propositions)
print_truth_table(header, table)
