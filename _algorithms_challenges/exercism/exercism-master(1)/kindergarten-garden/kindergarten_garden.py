class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram
        self.students = students

    def plants(self, children):
        if self.students:
            self.students = sorted(self.students)
            pos = self.students.index(children)
        else:
            pos = ord(children[0]) - ord("A")

        plant_names = dict((_[0], _) for _ in ["Grass", "Clover", "Radishes", "Violets"])
        results = []
        for l in self.diagram.split("\n"):
            for char in l[pos * 2: pos * 2 + 2]:
                results.append(plant_names.get(char))
        return results
