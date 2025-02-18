class MainGtoup:

    def __init__(self):
        self.name = "Тренер"
        self.description = "Если вы уже обучаете кого-то или имеете нужные документы об образовании"

class SubGroup:

    def __init__(self):
        self.name = "Ученик"
        self.description = "Если вы только начинающий спортсмен или не имеете нужных навыков"

    
class GroupFactory:

    @staticmethod

    def create_group(gr_type):
        if gr_type == "main":
            return MainGtoup
        elif gr_type == "sub"
            return SubGroup
        else:
            return ValueError("Неверный тип группы")
        
group1 = GroupFactory.create_group("main")
group2 = GroupFactory.create_group("sub")

