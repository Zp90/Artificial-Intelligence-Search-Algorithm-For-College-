NodeG3 = {"Name": "G3"}
NodeG1 = {"Name": "G1"}
NodeG2 = {"Name": "G2"}
NodeB  = {"Name": "B"}
NodeE  = {"Name": "E"}
NodeF  = {"Name": "F"}
NodeP  = {"Name": "P"}
NodeM  = {"Name": "M"}
NodeN  = {"Name": "N"}
NodeJ  = {"Name": "J"}
NodeI  = {"Name": "I"}
NodeH  = {"Name": "H"}
NodeA  = {"Name": "A"}
NodeD  = {"Name": "D"}
NodeC  = {"Name": "C"}
NodeS  = {"Name": "S"}
NodeL  = {"Name": "L"}
NodeK  = {"Name": "K"}



NodeS.update({
    "NextNode1": {"Cost": 5, "GetNode": NodeA},
    "NextNode2": {"Cost": 5, "GetNode": NodeB},
    "NextNode3": {"Cost": 3, "GetNode": NodeF},
    "NextNode4": {"Cost": 7, "GetNode": NodeE},
})

NodeA.update({
    "NextNode1": {"Cost": 6, "GetNode": NodeH},
    "NextNode2": None,
    "NextNode3": None,
    "NextNode4": None,
})

NodeH.update({
    "NextNode1": {"Cost": 2, "GetNode": NodeF},
    "NextNode2": {"Cost": 3, "GetNode": NodeI},
    "NextNode3": {"Cost": 5, "GetNode": NodeG3},
    "NextNode4": None,
})

NodeG3.update({
    "NextNode1": {"Cost": 7, "GetNode": NodeN},
    "NextNode2": None,
    "NextNode3": None,
    "NextNode4": None,
})

NodeN.update({
    "NextNode1": {"Cost": 4, "GetNode": NodeI},
    "NextNode2": {"Cost": 3, "GetNode": NodeM},
    "NextNode3": None,
    "NextNode4": None,
})

NodeI.update({
    "NextNode1": {"Cost": 2, "GetNode": NodeF},
    "NextNode2": {"Cost": 6, "GetNode": NodeJ},
    "NextNode3": None,
    "NextNode4": None,
})

NodeF.update({
    "NextNode1": {"Cost": 4, "GetNode": NodeA},
    "NextNode2": {"Cost": 5, "GetNode": NodeE},
    "NextNode3": None,
    "NextNode4": None,
})

NodeE.update({
    "NextNode1": {"Cost": 4, "GetNode": NodeB},
    "NextNode2": {"Cost": 3, "GetNode": NodeD},
    "NextNode3": {"Cost": 5, "GetNode": NodeK},
    "NextNode4": None,
})

NodeJ.update({
    "NextNode1": {"Cost": 5, "GetNode": NodeN},
    "NextNode2": {"Cost": 2, "GetNode": NodeE},
    "NextNode3": None,
    "NextNode4": None,
})

NodeB.update({
    "NextNode1": {"Cost": 6, "GetNode": NodeC},
    "NextNode2": {"Cost": 3, "GetNode": NodeD},
    "NextNode3": None,
    "NextNode4": None,
})

NodeC.update({
    "NextNode1": {"Cost": 8, "GetNode": NodeG1},
    "NextNode2": None,
    "NextNode3": None,
    "NextNode4": None,
})

NodeG1.update({
    "NextNode1": None,
    "NextNode2": None,
    "NextNode3": None,
    "NextNode4": None,
})

NodeD.update({
    "NextNode1": {"Cost": 6, "GetNode": NodeC},
    "NextNode2": None,
    "NextNode3": None,
    "NextNode4": None,
})

NodeK.update({
    "NextNode1": {"Cost": 3, "GetNode": NodeD},
    "NextNode2": {"Cost": 7, "GetNode": NodeL},
    "NextNode3": {"Cost": 5, "GetNode": NodeM},
    "NextNode4": None,
})

NodeM.update({
    "NextNode1": {"Cost": 5, "GetNode": NodeJ},
    "NextNode2": {"Cost": 2, "GetNode": NodeG2},
    "NextNode3": {"Cost": 4, "GetNode": NodeP},
    "NextNode4": {"Cost": 4, "GetNode": NodeE},
})

NodeP.update({
    "NextNode1": {"Cost": 2, "GetNode": NodeN},
    "NextNode2": {"Cost": 3, "GetNode": NodeG2},
    "NextNode3": None,
    "NextNode4": None,
})

NodeL.update({
    "NextNode1": {"Cost": 3, "GetNode": NodeG1},
    "NextNode2": {"Cost": 5, "GetNode": NodeG2},
    "NextNode3": None,
    "NextNode4": None,
})

NodeG2.update({
    "NextNode1": {"Cost": 7, "GetNode": NodeG1},
    "NextNode2": {"Cost": 6, "GetNode": NodeK},
    "NextNode3": None,
    "NextNode4": None,
})



def UniformCostSearch(Goal:list,StarterNode:dict):
    NodeVisited = [StarterNode["Name"]]
    CurrentNode = StarterNode
    SmallestCost = 10000000
    Path = None
    
    def FindNextNode(CurrentNode:dict,NodeVisited:list,Cost:int):
       
        def FindNodeWithName(name):
            nonlocal SmallestCost, Path 
            if CurrentNode[name] != None and not CurrentNode[name]["GetNode"]["Name"] in NodeVisited:
                if not CurrentNode[name]["GetNode"]["Name"] in Goal:
                    VisitedUpdate = NodeVisited.copy()
                    VisitedUpdate.append(CurrentNode[name]["GetNode"]["Name"])
                    FindNextNode(
                        CurrentNode[name]["GetNode"],
                        VisitedUpdate,
                        Cost + CurrentNode[name]["Cost"],
                    )
                else:
                    VisitedUpdate = NodeVisited.copy()
                    VisitedUpdate.append(CurrentNode[name]["GetNode"]["Name"])
                    print(VisitedUpdate,Cost + CurrentNode[name]["Cost"])

                    if SmallestCost > Cost + CurrentNode[name]["Cost"]:
                        SmallestCost = Cost + CurrentNode[name]["Cost"]
                        Path = VisitedUpdate
                    FindNextNode(
                        CurrentNode[name]["GetNode"],
                        VisitedUpdate,
                        Cost + CurrentNode[name]["Cost"],
                    )

        FindNodeWithName("NextNode1")
        FindNodeWithName("NextNode2")
        FindNodeWithName("NextNode3")
        FindNodeWithName("NextNode4")    


    FindNextNode(CurrentNode,NodeVisited,0)
    return Path,SmallestCost

print("Shortest:",UniformCostSearch(["G1"],NodeS))
