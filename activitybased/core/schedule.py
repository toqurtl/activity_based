import pandas as pd
import networkx as nx
from .activity import Activity


class Schedule(nx.DiGraph):
    def __init__(self, **args):
        self.activity_dict = {}
        self.dependency_list = []
        self.planned_project_duration = -1

        # subnode type in networks
        self.critical_path = None

    def get_activity_from_file(self, activity_file_name):
        activity_pd = pd.read_csv(activity_file_name)
        for _, act_info in activity_pd.iterrows():
            act = Activity(**act_info.to_dict())
            self.activity_dict[act.id] = act

    def get_dependency_from_file(self, dependency_file_name):
        dependency_pd = pd.read_csv(dependency_file_name)
        for _, act_info in dependency_pd.iterrows():
            self.dependency_list.append(act_info.tolist())

    def to_list(self):
        return [act.to_list() for act in self.activity_dict.values()]

    def __str__(self):
        return_str = ''
        for act in self.activity_dict.values():
            return_str += act.__str__()+'\n'
        return return_str


