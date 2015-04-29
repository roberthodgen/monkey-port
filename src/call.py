
import webapp2

import json

import twilio.twiml


class CallHandler(webapp2.RequestHandler):
	def post(self):
		""" Handle an incoming call. """
		raw_digits = self.request.POST.get('Digits')
		digits = list()
		for char in raw_digits:
			digits.append(char)
		response = twilio.twiml.Response()
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


class NewCallHandler(webapp2.RequestHandler):
	def get(self):
		""" Return a message. """
		response = twilio.twiml.Response()
		with response.gather(
			action='/call/code',
			method='POST',
			numDigits=4,
			timeout=10
		) as g:
			g.say(
				'Please code in.',
				voice='alice',
				language='en-GB'
			)

		self.response.out.write(str(response))


APP = webapp2.WSGIApplication([
	webapp2.Route(
		'/call/code',
		handler=CallHandler,
		methods=['POST']
	), webapp2.Route(
		'/call/new',
		handler=NewCallHandler,
		methods=['GET']
	)
])