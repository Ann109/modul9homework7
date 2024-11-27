def is_prime(func):
        def wrapper(*args):
                sum_three = (2, 3, 6)
                result = sum(sum_three)
                print(result)
                if sum(args) != int:
                        return ('Простое')
                if sum(args) != float:
                        return ('Составное')
                
        return wrapper

@is_prime
def sum_three(*args):
        sum_ = sum(args)
        return sum_


result = sum_three(2, 3, 6)
print(result)
