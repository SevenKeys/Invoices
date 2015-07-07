from common.components.component import ViewComponent

test_groups = [{'id': 0, 'name': 'Undefined', 'products': [{'name': 'banana', 'id': 0}, {'name': 'cucumber', 'id': 1}]},
               {'id': 1, 'name': 'Second'},
               {'id': 2, 'name': 'Other', 'products': [{'name': 'wolverine', 'id': 3}, {'name': 'cougar', 'id': 4}]}]

class SortableListView(ViewComponent):
    def __init__(self):
        super(SortableListView, self).__init__('components/sortable_list.html')

    def get_test_groups(self):
        return test_groups
