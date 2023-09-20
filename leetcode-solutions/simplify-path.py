class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        new_path = path.split('/')
        for item in new_path:
            if item=='..':
                if stack:
                    stack.pop()
            elif item not in ('','.'):
                stack.append(item)
       
        return "/" + "/".join(stack)
             
# # C://user//asdf/asdf/asdfa/file.txt => [c, user, asdf, asdf, file.txt]

        
#         st = "ab//adf///aasdf/asdf"
#         print(st.split())
        