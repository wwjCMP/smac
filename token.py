# token.py

# Copyright (C) 2015 Greenweaves Software Oty Ltd

# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs.  If not, see <http://www.gnu.org/licenses/>.

import os.path
import time

class Token:
    def __init__(self,name):
        self.name=name
        self.timeformat="%a, %d %b %Y %H:%M:%S +0000"
    
    def exists(self):
       return os.path.isfile(self.name)
       
    def read(self,initial):
        if self.exists():
            with open(self.name,"r") as f:
                date_line=f.readline().strip(' \t\n\r')
                self.time=time.strptime(date_line, self.timeformat)
                return self.line2ints(f.readline().strip(' \t\n\r'))
        else:
            return initial
        
    def line2ints(self,line):
        return [int(s) for s in line.split(",")]
    
    def write(self,values):
        with open(self.name,"w") as f:
           ts=time.strftime(self.timeformat) 
           f.write(ts+"\n")
           f.write(self.list2str(values)+"\n")
           
    def list2str(self,values):
        result=""
        sep=""
        for el in values:
            result+=sep
            result+=str(el)
            sep=","
        return result    
    
    def precedes(self,other):
        return self.time<other.time
    
if __name__ == "__main__":
    t1=Token("foo.txt")
    print t1.read([0,1])
    t1.write([1,2])