from enum import Enum


class Activity(object):
    def __init__(self, **act):
        # basic information
        self.id = act.get('id')
        self.duration = act.get('duration')
        self.cost = act.get('cost')
        self.resource = act.get('resource')
        self.quantity = act.get('quantity')

        # calculated information
        self.successors_id_list = []
        self.predecessors_id_list = []
        self.cpm_value_dict = {}

    def to_list(self):
        return [self.id, self.duration]

    def __str__(self):
        return str(self.to_list())+str(self.cpm_value_dict)


class ActivityAttribute(Enum):
    ID = 'id'
    DURATION = 'duration'
    COST = 'cost'
    RESOURCE = 'resource'
    QUANTITY = 'quantity'

