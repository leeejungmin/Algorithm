def solution(record):
    answer = []
    user=dict()
    action=[]
    for i in record:     
        record_s = i.split(" ")
        if record_s[0] == "Enter":
            user[record_s[1]] = record_s[2]
        elif record_s[0] == "Leave":
            pass
        else:
            user[record_s[1]] = record_s[2]
        action.append([record_s[1],record_s[0]])
    for i in action:
        if i[1] == "Enter":
            answer.append(user[i[0]]+"님이 들어왔습니다.")
        elif i[1] == "Leave":
            answer.append(user[i[0]]+"님이 나갔습니다.")
    return answer


def is_name(name,user):
    if name in user.keys():
        return True
        

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
#["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
print(solution(record))

#why? Think and make total plan before doing and just typing and correcting
#make list of name, enter
#find name and change -> if name in name -> name[0] = name
#drop down every list
#don't forgive, and relax, think the way.

#lack of knowledge dic,
#organize each part -> make user name update -> make update of answer
