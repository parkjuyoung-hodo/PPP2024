#숫자를 입력 받아서 그 리스트를 출력하시오.숫자는 정수만 입력 받고, 자연수가 아닌 입력 값은 무시하시오.
#-1를 입력하면 입력을 더 이상받지 않고 현재까지 입력 받은 값을 출력하시오.또한 총 개수와 평균을 구하시오
list=[]
user_number=0
while user_number != -1:
     try:
         user_number=int(input("정수를 입력하시오:"))
         list.append(user_number)

     except:
         print('정수를 입력하지 않았습니다.')


     # print(len(list))
     # print(sum(list))
     if -1 in list:
         list.remove(-1)
         result=sum(list)/len(list)
         print(f"받은 리스트 평균 값은{result}입니다.")
         print(f"지금까지 받은 list 개수 :{len(list)}")


     if user_number == -1:
         break







