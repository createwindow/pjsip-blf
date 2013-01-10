# $Id: mod_call.py 2078 2008-06-27 21:12:12Z nanang $
import time
import imp
import sys
import inc_const as const
from inc_cfg import *

# Load configuration
cfg_file = imp.load_source("cfg_file", ARGS[1])

# Test body function
def test_func(t):
	callee = t.process[0]
	caller = t.process[1]

	# if have_reg then wait for couple of seconds for PUBLISH
	# to complete (just in case pUBLISH is used)
	if callee.inst_param.have_reg:
		time.sleep(1)
	if caller.inst_param.have_reg:
		time.sleep(1)

	# for i in range(0, 9):
	# Caller making call
	caller.send("M")
	caller.send("5")
	caller.send(t.inst_params[0].uri)
	caller.expect(const.STATE_CALLING)

	# Callee waits for call and answers with 180/Ringing
	# time.sleep(0.2)
	callee.expect(const.EVENT_INCOMING_CALL)
	for i in xrange(0,4):
		callee.send("a")
		callee.send("180")
		# callee.expect("SIP/2.0 180")
		# caller.expect("SIP/2.0 180")

		# Hangup call
		caller.send("h")
		# Callee answers with 200/OK
		callee.send("a")
		callee.send("200")
		time.sleep(0.5)
		callee.expect(const.EVENT_INCOMING_CALL)
		callee.send("]")
		caller.send("]")


	# Wait until calls are cleared in both endpoints
	# caller.expect(const.STATE_DISCONNECTED)
	# callee.expect(const.STATE_DISCONNECTED)


# Here where it all comes together
test = cfg_file.test_param
test.test_func = test_func

