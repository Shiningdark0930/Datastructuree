# 과제 2



def mmain():
    nums = input("Enter integers separated by spaces ==>")
    num = nums.split(' ')
    try:
        num = [int(item) for item in num]
        print("The sum of the input integers is ==>", calculatesum(num))
        mmain()
        

    except:
        if nums == 'done':
            print("program terminated.good bye!")
        else:
            print("must enter integers separated by spaces")
            mmain()


def calculatesum(nums):
    summ = 0
    summ += nums[0]
    del nums[0]
    if len(nums) == 0:
        return summ
    else:
        return summ + calculatesum(nums)

mmain()
    