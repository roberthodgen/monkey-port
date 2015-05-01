
import webapp2

import json

import twilio.twiml

import utilities


class CodeInputHandler(webapp2.RequestHandler):
	def post(self):
		""" Handle an incoming call. """
		raw_digits = self.request.POST.get('Digits')
		digits = list()
		for char in raw_digits:
			digits.append(char)
		response = twilio.twiml.Response()
		number_to_call = utilities.number_for_code(raw_digits)
		if number_to_call:
			response.say(
				'Your call is being transferred. Press the star key to hangup\
 on the dialed party',
				voice='alice',
				language='en-GB'
			)
			response.dial(
				number=number_to_call,
				action='/call/in-call',
				timeout=30,
				hangupOnStar=True
			)
		else:
			response.say(
				'You entered',
				voice='alice',
				language='en-GB'
			)
			for digit in digits:
				# Say each digit
				response.say(
					digit,
					voice='alice',
					language='en-GB'
				)
			response.say(
				'Goodbye',
				voice='alice',
				language='en-GB'
			)
			response.hangup()
		self.response.out.write(str(response))


class InConnectedCallHandler(webapp2.RequestHandler):
	def post(self):
		""" Used once an outbound call has been dialed. """
		call_status = self.request.POST.get('DialCallStatus')
		response = twilio.twiml.Response()
		if call_status:
			response.say(
				utilities.verbose_call_status(call_status),
				voice='alice',
				language='en-GB'
			)
		with response.gather(
			action='/call/code',
			method='POST',
			numDigits=4,
			timeout=10
		) as g:
			g.say(
				'Please code in',
				voice='alice',
				language='en-GB'
			)
		self.response.out.write(str(response))


class NewCallHandler(webapp2.RequestHandler):
	def post(self):
		""" Return a message. """
		response = twilio.twiml.Response()
		with response.gather(
			action='/call/code',
			method='POST',
			numDigits=4,
			timeout=10
		) as g:
			g.say(
				'Please code in',
				voice='alice',
				language='en-GB'
			)

		self.response.out.write(str(response))


APP = webapp2.WSGIApplication([
	webapp2.Route(
		'/call/code',
		handler=CodeInputHandler,
		methods=['POST']
	), webapp2.Route(
		'/call/new',
		handler=NewCallHandler,
		methods=['POST']
	), webapp2.Route(
		'/call/in-call',
		handler=InConnectedCallHandler,
		methods=['POST']
	)
])