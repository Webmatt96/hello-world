import datetime
import json
possibilities = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                 "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                 "0","1","2","3","4","5","6","7","8","9",
                 "`","~","!","@","#","$","%","^","&","*","(",")","-","_","=","+","{","[","]","}","/","?","<",">",","] # 87 characters
user = []

x = 1
while x < len(possibilities):
    begin = datetime.datetime.now()
    for i in range(0, len(possibilities)): # Every possible single-character combination
        user.append(possibilities[i])
                   
    for i in range(0, len(possibilities)): # Every possible double-character combination
        for a in range(0, len(possibilities)):
            user.append(possibilities[i] + possibilities[a])

    for i in range(0, len(possibilities)): # Every possible triple-character combination
        for a in range(0, len(possibilities)):
            for b in range(0, len(possibilities)):
                user.append(possibilities[i] + possibilities[a] + possibilities[b])

    for i in range(0, len(possibilities)): # Every possible four-character combination
        for a in range(0, len(possibilities)):
            for b in range(0, len(possibilities)):
                for c in range(0, len(possibilities)):
                    user.append(possibilities[i] + possibilities[a] + possibilities[b] + possibilities[c])            

    for i in range(0, len(possibilities)): # Every possible five-character combination
        for a in range(0, len(possibilities)):
            for b in range(0, len(possibilities)):
                for c in range(0, len(possibilities)):
                    for d in range(0, len(possibilities)):
                        user.append(possibilities[i] + possibilities[a] + possibilities[b] + possibilities[c] + possibilities[d])

    for i in range(0, len(possibilities)): # Every possible six-character combination
        for a in range(0, len(possibilities)):
            for b in range(0, len(possibilities)):
                for c in range(0, len(possibilities)):
                    for d in range(0, len(possibilities)):
                        for e in range(0, len(possibilities)):
                            user.append(possibilities[i] + possibilities[a] + possibilities[b] + possibilities[c] + possibilities[d] + possibilities[e])

    for i in range(0, len(possibilities)): # Every possible seven-character combination
        for a in range(0, len(possibilities)):
            for b in range(0, len(possibilities)):
                for c in range(0, len(possibilities)):
                    for d in range(0, len(possibilities)):
                        for e in range(0, len(possibilities)):
                            for f in range(0, len(possibilities)):
                                user.append(possibilities[i] + possibilities[a] + possibilities[b] + possibilities[c] + possibilities[d] + possibilities[e] + possibilities[f])                             

    for i in range(0, len(possibilities)): # Every possible eight-character combination
        for a in range(0, len(possibilities)):
            for b in range(0, len(possibilities)):
                for c in range(0, len(possibilities)):
                    for d in range(0, len(possibilities)):
                        for e in range(0, len(possibilities)):
                            for f in range(0, len(possibilities)):
                                for g in range(0, len(possibilities)):
                                    user.append(possibilities[i] + possibilities[a] + possibilities[b] + possibilities[c] + possibilities[d] + possibilities[e] + possibilities[f] + possibilities[g])

    for i in range(0, len(possibilities)): # Every possible nine-character combination
        for a in range(0, len(possibilities)):
            for b in range(0, len(possibilities)):
                for c in range(0, len(possibilities)):
                    for d in range(0, len(possibilities)):
                        for e in range(0, len(possibilities)):
                            for f in range(0, len(possibilities)):
                                for g in range(0, len(possibilities)):
                                    for h in range(0, len(possibilities)):
                                        user.append(possibilities[i] + possibilities[a] + possibilities[b] + possibilities[c] + possibilities[d] + possibilities[e] + possibilities[f] + possibilities[g] + possibilities[h])

    for i in range(0, len(possibilities)): # Every possible ten-character combination
        for a in range(0, len(possibilities)):
            for b in range(0, len(possibilities)):
                for c in range(0, len(possibilities)):
                    for d in range(0, len(possibilities)):
                        for e in range(0, len(possibilities)):
                            for f in range(0, len(possibilities)):
                                for g in range(0, len(possibilities)):
                                    for h in range(0, len(possibilities)):
                                        for j in range(0, len(possibilities)):
                                            user.append(possibilities[i] + possibilities[a] + possibilities[b] + possibilities[c] + possibilities[d] + possibilities[e] + possibilities[f] + possibilities[g] + possibilities[h] + possibilities[j])                                        

    for i in range(0, len(possibilities)): # Every possible eleven-character combination
        for a in range(0, len(possibilities)):
            for b in range(0, len(possibilities)):
                for c in range(0, len(possibilities)):
                    for d in range(0, len(possibilities)):
                        for e in range(0, len(possibilities)):
                            for f in range(0, len(possibilities)):
                                for g in range(0, len(possibilities)):
                                    for h in range(0, len(possibilities)):
                                        for j in range(0, len(possibilities)):
                                            for k in range(0, len(possibilities)):
                                                user.append(possibilities[i] + possibilities[a] + possibilities[b] + possibilities[c] + possibilities[d] + possibilities[e] + possibilities[f] + possibilities[g] + possibilities[h] + possibilities[j] + possibilities[k])                                        

    for i in range(0, len(possibilities)): # Every possible twelve-character combination
        for a in range(0, len(possibilities)):
            for b in range(0, len(possibilities)):
                for c in range(0, len(possibilities)):
                    for d in range(0, len(possibilities)):
                        for e in range(0, len(possibilities)):
                            for f in range(0, len(possibilities)):
                                for g in range(0, len(possibilities)):
                                    for h in range(0, len(possibilities)):
                                        for j in range(0, len(possibilities)):
                                            for k in range(0, len(possibilities)):
                                                for l in range(0, len(possibilities)):
                                                    user.append(possibilities[i] + possibilities[a] + possibilities[b] + possibilities[c] + possibilities[d] + possibilities[e] + possibilities[f] + possibilities[g] + possibilities[h] + possibilities[j] + possibilities[k] + possibilities[l])                                        

    for i in range(0, len(possibilities)): # Every possible thirteen-character combination
            for a in range(0, len(possibilities)):
                for b in range(0, len(possibilities)):
                    for c in range(0, len(possibilities)):
                        for d in range(0, len(possibilities)):
                            for e in range(0, len(possibilities)):
                                for f in range(0, len(possibilities)):
                                    for g in range(0, len(possibilities)):
                                        for h in range(0, len(possibilities)):
                                            for j in range(0, len(possibilities)):
                                                for k in range(0, len(possibilities)):
                                                    for l in range(0, len(possibilities)):
                                                        for m in range(0, len(possibilities)):
                                                            user.append(possibilities[i] + possibilities[a] + possibilities[b] + possibilities[c] + possibilities[d] + possibilities[e] + possibilities[f] + possibilities[g] + possibilities[h] + possibilities[j] + possibilities[k] + possibilities[l] + possibilities[m])

    for i in range(0, len(possibilities)): # Every possible fourteen-character combination
            for a in range(0, len(possibilities)):
                for b in range(0, len(possibilities)):
                    for c in range(0, len(possibilities)):
                        for d in range(0, len(possibilities)):
                            for e in range(0, len(possibilities)):
                                for f in range(0, len(possibilities)):
                                    for g in range(0, len(possibilities)):
                                        for h in range(0, len(possibilities)):
                                            for j in range(0, len(possibilities)):
                                                for k in range(0, len(possibilities)):
                                                    for l in range(0, len(possibilities)):
                                                        for m in range(0, len(possibilities)):
                                                            for n in range(0, len(possibilities)):
                                                                user.append(possibilities[i] + possibilities[a] + possibilities[b] + possibilities[c] + possibilities[d] + possibilities[e] + possibilities[f] + possibilities[g] + possibilities[h] + possibilities[j] + possibilities[k] + possibilities[l] + possibilities[m] + possibilities[n])

    for i in range(0, len(possibilities)): # Every possible fifteen-character combination
                for a in range(0, len(possibilities)):
                    for b in range(0, len(possibilities)):
                        for c in range(0, len(possibilities)):
                            for d in range(0, len(possibilities)):
                                for e in range(0, len(possibilities)):
                                    for f in range(0, len(possibilities)):
                                        for g in range(0, len(possibilities)):
                                            for h in range(0, len(possibilities)):
                                                for j in range(0, len(possibilities)):
                                                    for k in range(0, len(possibilities)):
                                                        for l in range(0, len(possibilities)):
                                                            for m in range(0, len(possibilities)):
                                                                for n in range(0, len(possibilities)):
                                                                    for o in range(0, len(possibilities)):
                                                                        user.append(possibilities[i] + possibilities[a] + possibilities[b] + possibilities[c] + possibilities[d] + possibilities[e] + possibilities[f] + possibilities[g] + possibilities[h] + possibilities[j] + possibilities[k] + possibilities[l] + possibilities[m] + possibilities[n] + possibilities[o])

                                                                    x = x+1
                                                                    
    with open("password_list.txt", "w") as file_handle:
        json.dump(user, file_handle)

    end = datetime.datetime.now()
    print(end - begin)
    print(len(user))
