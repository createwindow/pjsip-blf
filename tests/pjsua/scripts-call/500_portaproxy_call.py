# $Id: 301_ice_public_a.py 2392 2008-12-22 18:54:58Z bennylp $
#
from inc_cfg import *

# Note:
#	- need --dis-codec to make INVITE packet less than typical MTU
uas_args = "--null-audio --id=\"<sip:123020@192.168.195.36>\" --registrar=sip:192.168.195.36 " \
  " --username=123020 --password=zzzxxx123 --realm=192.168.195.36 --proxy=\"sip:192.168.195.36;lr\" " \
  " --rtp-port 0 --use-ice --max-calls 10 --local-port=5061 --ip-addr=192.168.195.36 --bound-add=192.168.195.36" \
  " --dis-codec=i --dis-codec=s --dis-codec=g"

uac_args = "--null-audio --id=\"<sip:123010@192.168.195.36>\" --registrar=sip:192.168.195.36 " \
	" --username=123010 --password=zzzxxx123 --realm=192.168.195.36 --proxy=\"sip:192.168.195.36;lr\" " \
	" --rtp-port 0 --use-ice --max-calls 10 --dis-codec=i --dis-codec=s --dis-codec=g"

test_param = TestParam(
		"ICE via public internet",
		[
			InstanceParam(	"callee", uas_args,
					uri="<sip:123020@192.168.195.36>",
					have_reg=True, have_publish=False),
			InstanceParam(	"caller", uac_args,
					uri="<sip:123010@192.168.195.36>",
					have_reg=True, have_publish=False),
		]
		)

