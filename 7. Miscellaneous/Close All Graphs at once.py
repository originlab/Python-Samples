'''
This sample shows how to close all graphs at once by LabTalk script
'''
import originpro as op

# doc -e: execute the script in {} for all graph window (LP)
# win -cp: post a message to close the window
op.lt_exec("doc -e LP {win -cp %H}")