from owlready2 import *

onto = get_ontology("containment.rdf").load()



with onto:
    object = onto.Object("object")
    object1 = onto.Object("object1")
    drawer = onto.Drawer("drawer1")
    dresser = onto.Dresser("dresser1")

    drawer.part_of = [dresser]
    object1.inside_of = [drawer]
    object.inside_of = [object1]


    sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True)

    print(object.inside_of)