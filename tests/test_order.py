import src.orderer


def test_addOrderer():
    print(len(src.orderer.tabOrdered))
    src.orderer.addOrdered(1, 1, "Michel")
    print(len(src.orderer.tabOrdered))

def test_deleteOrderer():
    print(len(src.orderer.tabOrdered))
    src.orderer.deleteOrdered(1)
    print(len(src.orderer.tabOrdered))


