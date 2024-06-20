jina = ['banana', 'mangoes', 'apples']
# for i in range(5):
#     print(i, jina[i])
try:
    for i in range (5):
        print(jina[i])
except IndexError as e:
    print(f'An error has occurred {e}')
finally:
    print('Run complete')

# try:
#     result = 1 / 0
#     print(1 / 0)
# except ZeroDivisionError as e:
#     print(f'An error has occurred {e}')
# finally:
#     print('This will always be printed')
