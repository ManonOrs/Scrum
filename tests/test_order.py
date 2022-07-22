from src import orderer


def testAddOrdered():
    assert len(orderer.tabOrdered) == 0
    orderer.addOrdered(1, 1, "Michel")
    assert len(orderer.tabOrdered) == 1

def testDeleteOrdered():
    assert len(orderer.tabOrdered) == 1
    orderer.deleteOrdered(1)
    assert len(orderer.tabOrdered) == 0

def testAddPlat():
    orderer.tabOrdered.append(orderer.Ordered(1, 1, "Michel"))
    assert len(orderer.tabOrdered[0].plats) == 0
    orderer.tabOrdered[0].addPlat("pizza")
    assert len(orderer.tabOrdered[0].plats) == 1

def testDeletePlat():
    assert len(orderer.tabOrdered[0].plats) == 1
    orderer.tabOrdered[0].deletePlat("pizza", 0)
    assert len(orderer.tabOrdered[0].plats) == 0

def testModifyOrderedAdd(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "pizza")
    orderer.modifyOrdered(1,"add")
    assert len(orderer.tabOrdered[0].plats) == 1

def testModifyOrderedDelete(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "pizza")
    orderer.modifyOrdered(1,"delete")
    assert len(orderer.tabOrdered[0].plats) == 0
