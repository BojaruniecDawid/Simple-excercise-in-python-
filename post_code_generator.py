def code_generator(code1, code2):
    code1_list= code1.split('-')
    code2_list = code2.split('-')

    code1_list = [int(item) for item in code1_list]
    code2_list = [int(item) for item in code2_list]

    while not code1_list == code2_list:
        if code1_list[1] < 999:
            code1_list[1] += 1
            if code1_list[1] < 10:
                print("{}-00{}".format(code1_list[0], code1_list[1]))
            elif code1_list[1] < 100:
                print("{}-0{}".format(code1_list[0], code1_list[1]))
            else:
                print("{}-{}".format(code1_list[0], code1_list[1]))

        else:
            code1_list[0] += 1
            code1_list[1] = 0
            print("{}-00{}".format(code1_list[0], code1_list[1]))


code_generator('79-900', '80-155')