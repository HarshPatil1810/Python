class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_log=[]
        digit_logs=[]
        
        for log in logs:
            identifier,rest=log.split(" ",1)
            if rest[0].isdigit():
                digit_logs.append(log)
            else:
                letter_log.append((rest, identifier, log))
            
        letter_log.sort(key=lambda x:( x[0],x[1]))
        return [log[2] for log in letter_log] + digit_logs
