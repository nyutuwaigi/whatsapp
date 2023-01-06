import pywhatkit

numbers = [+12729001768,+13024209552,+13037252050,+13172178201,+13204930508,+13344474938,+14083332243,+14085813357,+14088062050,+14088062957,+14088063690,+14088066056,+14088068699,+14088069298,+14088069991,+14088073728,+14088074764,+14088075904,+14088077910,+14088079425,+14088131748,+14088135387,+14088135484,+14088138117,+14088139027,+14088160151,+14088166671,+14088210585,+14088211617,+14088211759,+14088212105,+14088212536,+14088213370,+14088213472,+14088213500,+14088213907,+14088214764,+14088216138,+14088218665,+14088218805,+14088230191,+14088231274,+14088231363,+14088232070,+14088232551,+14088232822,+14088234661,+14088235565,+14088236105,+14088237469,+14088238724,+14088238801,+14088239885,+14088239889,+14088261132,+14088267230,+14088267793,+14088269048,+14088282806,+14088285998,+14088288077,+14088288099,+14088288804,+14088288954,+14088290385,+14088290794,+14088291119,+14088291163,+14088291266,+14088291393,+14088291941,+14088299929,+14088299987,+14088307851,+14088321439,+14088322939,+14088326340,+14088326965,+14088327896,+14088328700,+14088328915,+14088329081,+14088329464,+14088329954,+14088330198,+14088330334,+14088330404,+14088332679,+14088333456,+14088345688,+14088345712,+14088345900,+14088346727,+14088349661,+14088352985,+14088353812,+14088354075,+14088355294,+14088355483,+14088361118,+14088362169,+14088362587,+14088364820,+14088366592,+14088368185,+14088380022,+14088381876,+14088382171,+14088382223,+14088382904,+14088383645,+14088385205,+14088386094,+14088386383,+14088387658,+14088388133,+14088389317,+14088389487,+14088390439,+14088392700,+14088392986,+14088393538,+14088395388,+14088396268,+14088396876,+14088397609,+14088397739,+14088399075,+14088399129,+14088406385,+14088412780,+14088416529,+14088416807,+14088437271,+14088437552,+14088491412,+14088495010,+14088496021,+14088497839,+14088540516,+14088542559,+14088549717,+14088573908,+14088574240,+14088574636,+14088574684,+14088575698,+14088575749,+14088575903,+14088579528,+14088583300,+14088584284,+14088585031,+14088586003,+14088588016,+14088588522,+14088589304,+14088592150,+14088592889,+14088594761,+14088596229,+14088599525,+14582717476,+15203710537,+15638891757,+15705208596,+15705404104,+15705406348,+15743292749,+15752609888,+15869446908,+16057401066,+16069634117,+16074313723,+16629778344,+16784585009,+17206940422,+17245139015,+17247346469,+17272839322,+17313133478,+17472309793,+17572175267,+17622904523,+17656823164,+17656823831,+18028390824,+18028398826,+18052041572,+18702125918,+18708480622,+19016560672,+19039216372,+19039980984,+19203137066,+19409010237,+19863138005,+12603874039,+12729001768,+13024209552,+13037252050,+13172178201,+13204930508,+13344474938,+14083332243,+14085813357,+14088062050,+14088062957,+14088063690,+14088066056,+14088068699,+14088069298,+14088069991,+14088073728,+14088074764,+14088075904,+14088077910,+14088079425,+14088131748,+14088135387,+14088135484,+14088138117,+14088139027,+14088160151,+14088166671,+14088210585,+14088211617,+14088211759,+14088212105,+14088212536,+14088213370,+14088213472,+14088213500,+14088213907,+14088214764,+14088216138,+14088218665,+14088218805,+14088230191,+14088231274,+14088231363,+14088232070,+14088232551,+14088232822,+14088234661,+14088235565,+14088236105,+14088237469,+14088238724,+14088238801,+14088239885,+14088239889,+14088261132,+14088267230,+14088267793,+14088269048,+14088282806,+14088285998,+14088288077,+14088288099,+14088288804,+14088288954,+14088290385,+14088290794,+14088291119,+14088291163,+14088291266,+14088291393,+14088291941,+14088299929,+14088299987,+14088307851,+14088321439,+14088322939,+14088326340,+14088326965,+14088327896,+14088328700,+14088328915,+14088329081,+14088329464,+14088329954,+14088330198,+14088330334,+14088330404,+14088332679,+14088333456,+14088345688,+14088345712,+14088345900,+14088346727,+14088349661,+14088352985,+14088353812,+14088354075,+14088355294,+14088355483,+14088361118,+14088362169,+14088362587,+14088364820,+14088366592,+14088368185,+14088380022,+14088381876,+14088382171,+14088382223,+14088382904,+14088383645,+14088385205,+14088386094,+14088386383,+14088387658,+14088388133,+14088389317,+14088389487,+14088390439,+14088392700,+14088392986,+14088393538,+14088395388,+14088396268,+14088396876,+14088397609,+14088397739,+14088399075,+14088399129,+14088406385,+14088412780,+14088416529,+14088416807,+14088437271,+14088437552,+14088491412,+14088495010,+14088496021,+14088497839,+14088540516,+14088542559,+14088549717,+14088573908,+14088574240,+14088574636,+14088574684,+14088575698,+14088575749,+14088575903,+14088579528,+14088583300,+14088584284,+14088585031,+14088586003,+14088588016,+14088588522,+14088589304,+14088592150,+14088592889,+14088594761,+14088596229,+14088599525,+14582717476,+15203710537,+15638891757,+15705208596,+15705404104,+15705406348,+15743292749,+15752609888,+15869446908,+16057401066,+16069634117,+16074313723,+16629778344,+16784585009,+17206940422,+17245139015,+17247346469,+17272839322,+17313133478,+17472309793,+17572175267,+17622904523,+17656823164,+17656823831,+18028390824,+18028398826,+18052041572,+18702125918,+18708480622,+19016560672,+19039216372,+19039980984,+19203137066,+19409010237,+19863138005]

i=0

while True:

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 21, 7
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)
    
    pywhatkit.sendwhatmsg(numbers[i], 'Selenium test', 20, 5
    )
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)

    pywhatkit.sendwhatmsg_instantly(numbers[i], 'Selenium test')
    # driver.find_element_by_xpath('//span[@iconclass="send"]').click()
    i=i+1
    # time.sleep(2)


    