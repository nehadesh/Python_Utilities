currFile = None
   file = None
   with open('search.txt', 'r') as infile:
      for line in infile:
         if line.startswith("Group:"):
            if file:
               file.close()
            words = line.split()
            words = words[1:]
            fileName = 'search_strings/'
            name = ' '.join(words)
            fileName = fileName + name + '.txt'
            currFile = fileName
            file = open(fileName, 'w')
      elif line.startswith("EOF!!!"):
         break
      else:
         file.write(line)
