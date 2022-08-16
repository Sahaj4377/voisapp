import pandas as pd




df = pd.read_csv("C:\\Users\\Sahaj's PC\\PycharmProjects\\pythonProject4\\data.csv")


            dict = {'firstname': ["sahaj","ganu"], 'lastname': ["cha","pandw"]}
                    #df = pd.DataFrame({'firstname': [], 'lastname': []})


                #df.loc[len(df.index)] = [firstname,lastname]
            df = df.append(dict,ignore_index=True)
            df