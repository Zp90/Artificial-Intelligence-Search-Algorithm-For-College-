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










HeuristicTable = {
"G1" : {
"S" : 3.00,
"A" : 3.80,
"B" : 2.10,
"C" : .90,
"D" : 1.30,
"E" : 2.10,
"F" : 3.20,
"H" : 3.80,
"I" : 3.50,
"J" : 2.80 ,
"K" : 1.60,
"L" : 1.00 ,
"M" : 2.20,
"N" : 3.20 ,
"P" : 2.70,
"G1" : 0,
"G2" : 1.70,
"G3" : 4.20,},




"G2" : {
"S" : 3.10 ,
"A" : 3.90 ,
"B" : 2.60 ,
"C" : 2.10 ,
"D" : 1.70 ,
"E" : 1.90  ,
"F" : 2.80 ,
"H" : 3.30 ,
"I" : 2.70 ,
"J" : 1.90 ,
"K" : 1.10 ,
"L" : .90 ,
"M" : .90 ,
"N" : 1.90 ,
"P" : 1.00 ,
"G1" : 1.70 ,
"G2" :  0,
"G3" : 3.50 ,},





"G3" : {
"S" : 2.70  ,
"A" : 2.50  ,
"B" : 3.50  ,
"C" : 3.90  ,
"D" : 3.30  ,
"E" : 2.50  ,
"F" : 1.90  ,
"H" : 1.30  ,
"I" : 1.00  ,
"J" : 1.70  ,
"K" : 2.80  ,
"L" : 3.50  ,
"M" : 2.60  ,
"N" : 1.60  ,
"P" : 2.80 ,
"G1" : 4.20 ,
"G2" :  3.50 ,
"G3" : 0,}
}






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


def BestFirstSearch(Starter:vars,Goal:list):
    Path = [Starter["Name"]]
    def CheckNextNode(Node):
        NextNode = None
        SmallestValue = 10000000
        def CheckHeuristicValue(Name):
            nonlocal SmallestValue,NextNode
            if Node[Name] != None:
                NextNodeName = Node[Name]["GetNode"]['Name']
                HeuristicValue = HeuristicTable[Goal[0]][NextNodeName] # h(n)
                if HeuristicValue < SmallestValue:
                    NextNode = Node[Name]["GetNode"]
                    SmallestValue = HeuristicValue
                   
        if not Node["Name"] in Goal:
            CheckHeuristicValue("NextNode1")
            CheckHeuristicValue("NextNode2")
            CheckHeuristicValue("NextNode3")
            CheckHeuristicValue("NextNode4")
            Path.append(NextNode["Name"])
            return CheckNextNode(NextNode)
        else:
            return 
    CheckNextNode(Starter)


    #Get Cost
    def CalculateCost(Starter,Path):
        Cost = 0
        def Search(Starter,i):
            nonlocal Cost
            if i == len(Path):
                return
            if Starter["NextNode1"] != None and Starter["NextNode1"]["GetNode"]["Name"] == Path[i]:
                Cost += Starter["NextNode1"]["Cost"] 
                Search(Starter["NextNode1"]["GetNode"],i+1)
            elif Starter["NextNode2"] != None and Starter["NextNode2"]["GetNode"]["Name"] == Path[i]:
                Cost += Starter["NextNode2"]["Cost"] 
                Search(Starter["NextNode2"]["GetNode"],i+1)
            elif Starter["NextNode3"] != None and Starter["NextNode3"]["GetNode"]["Name"] == Path[i]:
                Cost += Starter["NextNode3"]["Cost"] 
                Search(Starter["NextNode3"]["GetNode"],i+1)
            elif Starter["NextNode4"] != None and Starter["NextNode4"]["GetNode"]["Name"] == Path[i]:
                Cost += Starter["NextNode4"]["Cost"] 
                Search(Starter["NextNode4"]["GetNode"],i+1)
        
        Search(Starter,0+1)
        return Cost
    
    return Path,CalculateCost(Starter,Path)

print(BestFirstSearch(NodeS,["G1","G2","G3"]))