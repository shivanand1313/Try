
1# KBC Game
b1 = "Mumbai"
a1 = "Shiv"
a2 = "Start - up"
a3 = "25"
listq = ["What is Capital of Maharashtra? ", "What is my Name? ", "What is my Goal?", "What is my Age?"]
listans = [b1, a1, a2, a3]
opt1 = ["Nagpur", "Arya", "N_Core Job", "18"]
opt2 = ["Pune", "Sai", "Core Job", "28"]
opt3 = ["Nashik", "Raj", "Nothing", "32"]
t = 0
try:
    k = 0
    while k < 4:
        try:
            for i in range(k - 1, k):
                que = listq[k - 1]
                print(que)
                op = {opt3[k - 1], opt2[k - 1], listans[k - 1], opt1[k - 1]}
                opt = list(op)
                print("1 = " + opt[0], "        2 = " + opt[1], "\n3 = " + opt[2], "        4 = " + opt[3])
                ns = int(input("Select the correct option "))
                ians = opt[ns - 1]
                ans = listans[k - 1]
                if ians == ans:
                    print("Aap ka jawab sahi hai ")
                    t = t + 1
                    if t == 2:
                        print("you have won Rs. 10,000")
                    elif t == 3:
                        print("you have won Rs. 3,20,000")
                    elif t == 4:
                        print("you have won Rs. 50,00,00,000")
                    continue
                elif ians != ans:
                    print("Galat jawab")
                    z = 100
                    while z > 0:
                        sahi = int(input("Sahi Jawab ke liye 1 dabay "))
                        if sahi == 1:
                            print("Sahi jawab hai " + ans)
                            break
                        else:
                            z = z + 1
                    continue
                else:
                    continue

        except:
            print("Invalid input!")
        k = k + 1
except:
    print("Invalid input!")

finally:
    if t == 4:
        print("Aap ke account me Rs. 50,00,00,000 bhej diye gaye hai")
        Won = "\n-------------------App Crorepati Banchuke Ho-------------------\n"
        pri = Won.center(60)
        print(pri)
    elif t == 3:
        print("Aap ke account me Rs. 3,20,000 bhej diye gaye hai")
    elif t == 2:
        print("Aap ke account me Rs. 1 Crore bhej diye gaye hai")
    else:
        print("Aap game khelne ke paatrata nahi rakte")

    print("Game Over")