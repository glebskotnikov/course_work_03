class Operations:
    """
    Класс операций со счетами и картами
    """

    def __init__(self, id_, date, state, operationAmount, description, to_, from_=None):
        self.id_ = id_
        self.date = date
        self.state = state
        self.operationAmount = operationAmount
        self.description = description
        self.from_ = from_
        self.to_ = to_

    def __repr__(self):
        return f'Operations(id_={self.id_}, ' \
               f'date={self.date}, ' \
               f'state={self.state}, ' \
               f'operationAmount={self.operationAmount}, ' \
               f'description={self.description}, ' \
               f'from={self.from_}, ' \
               f'to={self.to_})'

    def __eq__(self, other):
        return self.id_ == other.id_ and \
            self.date == other.date and \
            self.state == other.state and \
            self.operationAmount == other.operationAmount and \
            self.description == other.description and \
            self.from_ == other.from_ and \
            self.to_ == other.to_
