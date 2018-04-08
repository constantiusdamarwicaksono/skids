import sys, csv, json
from pprint import pprint

def clean_array(arr):
    clean = []
    for element in arr:
        if element != "":
            element = element.strip().strip(",")
            if "(" in element :
                clean = clean + list(map(lambda s:s.strip(")").strip(",").strip("BYTE"),element.split("(")))
                continue
            clean.append(element.strip())
    return clean

def main():
    tree = {}
    table_name = ""
    filename = sys.argv[1]
    with open(filename) as file:
        result = open(filename[:-3]+"csv","w",newline="")
        csvwriter = csv.writer(result,delimiter=";",quotechar=" ",quoting=csv.QUOTE_MINIMAL);
        start = False
        for line in file:
            clean_line = line[:-1]
            if "CREATE TABLE" in clean_line:
                table_name =  clean_line.split(" ")[2]
                print(table_name)
                csvwriter.writerow([table_name])
                tree[table_name]={}
                continue
            if clean_line == "(":
                start = True
                continue
            elif clean_line == ")":
                start = False
                csvwriter.writerow([])
            if start :
                #print(clean_array(clean_line.split("  ")))
                row_array = clean_array(clean_array(clean_line.split("  ")))
                row_array.append(" ")
                # print(len(row_array))
                if len(row_array) < 4:
                    row_array.append(" ")
                if "NOT NULL" in row_array[len(row_array)-2]:
                    del row_array[len(row_array)-2]
                    row_array.append("M")
                else:
                    row_array.append("O")
                print(row_array)
                csvwriter.writerow(row_array)
                tree[table_name][row_array[0]]=row_array[1:]
        file.close()
        result.close()
        pprint(tree)
        with open(filename[:-3]+"json",'w+') as outjson:
            outjson.write(json.dumps(tree))
            outjson.close()

if __name__ == "__main__":
    main()
