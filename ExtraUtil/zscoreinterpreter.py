# -*- coding: utf-8 -*-

def calcZscore(result_list, mean_list, sd_list):
    #finds out which SD interval patient result is in and orders it in a list
    z_score_list = []
    for i in range(len(result_list)):
        if sd_list[i] == 0:
            sd_list[i] = 0.00000001 #protects the program from failing
        z_score = ((result_list[i] - mean_list[i]) / sd_list[i])
        z_score_list.append(float("%.2f" % z_score))
    return z_score_list

def calcPercentile(z_score_list):
    #gets the Z score list, changes it into percentile list
    import math

    def percentile(z_score):
        return .5 * (math.erf(z_score / 2 ** .5) + 1)

    perc_list = []
    for i in range(len(z_score_list)):
        try:
            perc_temp = str("%.2f" % (100 * float(percentile(z_score_list[i]))))
            perc_list.append(perc_temp)
        except:
            print("Persentil hesaplanırken bir hata oluştu.")
            pass

    return perc_list
    
def outputPrintlist(result_list, z_score_list, z_score_verbal_list, perc_list):
    #puts all the lists in their proper, more manageable order to print in CSV
    printable_list = []
    for y in range(len(result_list)):
        if not result_list[y] in ["999", 999, 999.0, "999.0"]:
            printable_list.append(result_list[y])
            if not float(z_score_list[y]) in [999.0, -999.0]:
                printable_list.append(z_score_list[y])
                printable_list.append(perc_list[y])
                printable_list.append(z_score_verbal_list[y])
            else:
                printable_list.append("N/A")
                printable_list.append("N/A")
                printable_list.append("N/A")
        else:
            printable_list.append("N/A")
            printable_list.append("N/A")
            printable_list.append("N/A")
            printable_list.append("N/A")
    return printable_list

def outputConsole_results(result_list, z_score_list, z_score_verbal_list, perc_list):
    #gets the results ready to print onto the screen
    console_result = []
    
    for i in range(len(z_score_list)):
        if (result_list[i] != 999.00) and (999.00 != float(z_score_list[i])) and (-999.00 != float(z_score_list[i])):
            console_result.append("Hastanın puanı: " + str(result_list[i]) + " - " + 
            str(z_score_verbal_list[i]) + " Z skoru: " + str(z_score_list[i]) + " - Persentil: " + str(perc_list[i]))
            
        elif (result_list[i] != 999.00) and ((999.00 == float(z_score_list[i])) or (-999.00 == float(z_score_list[i]))):
            console_result.append("Hastanın puanı: " + str(result_list[i]) + " - Bu parametreye ait norm verisi yoktur.")
        
        else:
            console_result.append("Bu basamak uygulanmamış veya uygulanamamıştır.")

    return console_result


def zScoreToVerbal(z_score_list): 
    #assumes Z scores get better as it goes up, multiply with "-1" if otherwise before using this function
    z_score_verbal_list = []
    if settings("zInterval") == "0-1":
        for i in range(len(z_score_list)):
            if z_score_list[i] >= -1:
                x = "Normal."
            elif -2 <= z_score_list[i] < -1:
                x = "Hafif derecede bozulma."
            elif -3 <= z_score_list[i] < -2:
                x = "Orta derecede bozulma."
            elif z_score_list[i] < -3 and z_score_list[i] != 999:
                x = "Ağır derecede bozulma." 
            else:
                x = "Bu grup için norm değeri bulunmamaktadır."
            z_score_verbal_list.append(x)
    
    if settings("zInterval") == "0-1.5":
        for i in range(len(z_score_list)):
            if z_score_list[i] >= -1.5:
                x = "Normal."
            elif -2 <= z_score_list[i] < -1.5:
                x = "Hafif derecede bozulma."
            elif -3 <= z_score_list[i] < -2:
                x = "Orta derecede bozulma."
            elif z_score_list[i] < -3 and z_score_list[i] != 999:
                x = "Ağır derecede bozulma." 
            else:
                x = "Bu grup için norm değeri bulunmamaktadır."
            z_score_verbal_list.append(x)
    
    return z_score_verbal_list


def zScoreInterpreter(z_score_list, z_score_legend):
    #z_score_legend = {"all":"less"} or {"all":"more"} means the all the Z scores
    # get better as they go lower or higher
    #z_score_legend = {"0":"less", "1":"more", "2":"less"} means 0 and 2nd Z scores
    # get better as they go low and 1 gets better when high
    z_score_verbal_list = []
    perc_list = []
    temp_z_score_list = []
    try:
        if z_score_legend["all"] == "more":          
            temp_z_score_list = z_score_list
                    
        elif z_score_legend["all"] == "less":
            for i in range(len(z_score_list)):
                temp_z_score_list[i] = -1 * z_score_list[i]
            
    except:
        for i in z_score_legend.keys():
            if z_score_legend[i] == "more":
                temp_z_score_list[int(i)] = z_score_list[int(i)]
                
            elif z_score_legend[i] == "less":
                temp_z_score_list[int(i)] = -1 * z_score_list[int(i)]
                
    
    perc_list = calcPercentile(temp_z_score_list)
            
    z_score_verbal_list = zScoreToVerbal(temp_z_score_list)
    
    
    return perc_list, z_score_verbal_list
    
    
    
    
    
xyz = {}    
for i in range(20):
    xyz[i] = "less"
    
print(xyz)    
    