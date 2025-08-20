
"""
(1)
* * * * *    

n=5
for i in range(n):
    print("*",end=" ")
"""

"""
(2)
*
*
*
*

n=5 
for i in range(n):
    print("* ")
"""
"""
(3)
* * * *
* * * *
* * * *
* * * * 

n=4

for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
"""

"""
(4)
* 
* *
* * *
* * * * 
* * * * * 

n=5

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
"""

"""
(5)
* * * * * 
* * * *
* * * 
* * 
*

n=5 
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()
"""

"""
(6)
     *
    **
   ***
  ****
 *****

n=5

for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()
"""

"""
(7)
  * * * * * 
    * * * *
      * * *
        * *
          *
n=5

for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(i,n):
        print("*",end=" ")
    print()
"""

"""
(8)
          * 
        * * *
      * * * * * 
    * * * * * * *
  * * * * * * * * *

n=5

for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    for l in range(i):
        print("*",end=" ")
    print()
"""

"""
(9)
* * * * * * * * * 
  * * * * * * *
    * * * * * 
      * * *
        *

n=5

for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(i,n):
        print("*",end=" ")
    for l in range(i,n-1):
        print("*",end=" ")
    print()
"""

"""
(10)
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

n=5

for i in range(n):
    for j in range(i+1,n):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    for l in range(i):
        print("*",end=" ")
    print()

q=4
for m in range(q):
    for r in range(m+1):
        print(" ",end=" ")
    for p in range(m+1,q):
        print("*",end=" ")
    for s in range(q-m):
        print("*",end=" ")
    print()
    
"""
"""
(11)
           *  
         *   *
       *   *   *
     *   *   *   *  
   *   *   *   *   *

n=5 

for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(i+1):
        print(" * ",end=" ")
    print()
"""
"""
(12)
           *                   *
         *   *               *   *
       *   *   *           *   *   *
     *   *   *   *       *   *   *   *
   *   *   *   *   *   *   *   *   *   *

n=5 

for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(i+1):
        print(" * ",end=" ")
    for l in range(i,n-1):
        print("   ",end=" ")
        
    for o in range(i+1):
        print(" * ",end=" ")
    for l in range(i):
        print(" ",end=" ")
    print()
"""

"""
(13)
 *   *   *   *   *  
   *   *   *   *
     *   *   *
       *   *
         *
         *
       *   *
     *   *   *  
   *   *   *   *
 *   *   *   *   *

n=5

for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range(i,n):
        print(" * ",end=" ")
    print()
    
for l in range(n):
    for m in range(l,n-1):
        print(" ",end=" ")
    for o in range(l+1):
        print(" * ",end=" ")
    print()
"""

"""
(14)
*             * 
* *         * *
* * *     * * *
* * * * * * * *
* * *     * * *
* *         * *
*             *

n=4

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for k in range(i,n-1):
        print("   ",end=" ")
    for l in range(i+1):
        print("*",end=" ")
    print()
    
for m in range(n):
    for o in range(m,n-1):
        print("*",end=" ")
    for p in range(m+1):
        print("   ",end=" ")
    for q in range(m,n-1):
        print("*",end=" ")
    print()
"""
