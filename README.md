# EGA-API-Python-Wrapper
This is the python wrapper for the EGA API, in order that it will be more friendly to use.

If you want to use this code, please add "from EGA import Session" to your code.

The main class is 'Session'.

When initializing a dialogue, newSession = newSession()

The operations of API has been sorted in a hierarchical way.

The operations of the top level will be: enumerate, retrieve, submit and logout.

The operations in each top level operation has also been sorted in a hierarchical way.

For example, metadata and files are the top level opertions in retrieve, in this way, newSession.retrieve.metadata.dacs will be very intuitive.

More examples are like: newSession.submit.validateOne.policy, newSession.submit.submitOne.run