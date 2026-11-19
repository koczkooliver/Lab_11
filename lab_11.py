from mindmap_composite import MindMapComposite
from mindmap_leaf import MindMapLeaf


def main():

    root = MindMapComposite("Python Programming", "circle")

    basics = MindMapComposite("Python Basics", "oval")
    basics.add(MindMapLeaf("Variables","plain"))
    basics.add(MindMapLeaf("Strings", "plain"))
    basics.add(MindMapLeaf("Numbers", "plain"))
    basics.add(MindMapLeaf("Booleans", "plain"))
    root.add(basics)

    functions = MindMapComposite("Functions", "square")
    functions.add(MindMapLeaf("Objects", "plain"))
    functions.add(MindMapLeaf("__init__", "plain"))
    functions.add(MindMapLeaf("__str__", "plain"))
    root.add(functions)

    skills = MindMapComposite("Programming Skills", "hexagon")
    skills.add(MindMapLeaf("Problem Solving", "plain"))
    skills.add(MindMapLeaf("Debugging", "plain"))
    skills.add(MindMapLeaf("Writing code", "plain"))
    root.add(skills)

    root.display()

if __name__ == "__main__":
    main()