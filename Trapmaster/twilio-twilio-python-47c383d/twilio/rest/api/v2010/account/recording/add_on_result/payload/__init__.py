# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class PayloadList(ListResource):

    def __init__(self, version, account_sid, reference_sid, add_on_result_sid):
        """
        Initialize the PayloadList

        :param Version version: Version that contains the resource
        :param account_sid: The unique sid that identifies this account
        :param reference_sid: A string that uniquely identifies the recording.
        :param add_on_result_sid: A string that uniquely identifies the result

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadList
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadList
        """
        super(PayloadList, self).__init__(version)

        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'reference_sid': reference_sid,
            'add_on_result_sid': add_on_result_sid,
        }
        self._uri = '/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{add_on_result_sid}/Payloads.json'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams PayloadInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists PayloadInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of PayloadInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of PayloadInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadPage
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return PayloadPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a PayloadContext

        :param sid: Fetch by unique payload Sid

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadContext
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadContext
        """
        return PayloadContext(
            self._version,
            account_sid=self._solution['account_sid'],
            reference_sid=self._solution['reference_sid'],
            add_on_result_sid=self._solution['add_on_result_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a PayloadContext

        :param sid: Fetch by unique payload Sid

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadContext
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadContext
        """
        return PayloadContext(
            self._version,
            account_sid=self._solution['account_sid'],
            reference_sid=self._solution['reference_sid'],
            add_on_result_sid=self._solution['add_on_result_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.PayloadList>'


class PayloadPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the PayloadPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The unique sid that identifies this account
        :param reference_sid: A string that uniquely identifies the recording.
        :param add_on_result_sid: A string that uniquely identifies the result

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadPage
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadPage
        """
        super(PayloadPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of PayloadInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadInstance
        """
        return PayloadInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            reference_sid=self._solution['reference_sid'],
            add_on_result_sid=self._solution['add_on_result_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.PayloadPage>'


class PayloadContext(InstanceContext):

    def __init__(self, version, account_sid, reference_sid, add_on_result_sid, sid):
        """
        Initialize the PayloadContext

        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param reference_sid: The reference_sid
        :param add_on_result_sid: The add_on_result_sid
        :param sid: Fetch by unique payload Sid

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadContext
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadContext
        """
        super(PayloadContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'reference_sid': reference_sid,
            'add_on_result_sid': add_on_result_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{add_on_result_sid}/Payloads/{sid}.json'.format(**self._solution)

    def fetch(self):
        """
        Fetch a PayloadInstance

        :returns: Fetched PayloadInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return PayloadInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            reference_sid=self._solution['reference_sid'],
            add_on_result_sid=self._solution['add_on_result_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the PayloadInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.PayloadContext {}>'.format(context)


class PayloadInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, reference_sid,
                 add_on_result_sid, sid=None):
        """
        Initialize the PayloadInstance

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadInstance
        """
        super(PayloadInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'add_on_result_sid': payload['add_on_result_sid'],
            'account_sid': payload['account_sid'],
            'label': payload['label'],
            'add_on_sid': payload['add_on_sid'],
            'add_on_configuration_sid': payload['add_on_configuration_sid'],
            'content_type': payload['content_type'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'reference_sid': payload['reference_sid'],
            'subresource_uris': payload['subresource_uris'],
        }

        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'reference_sid': reference_sid,
            'add_on_result_sid': add_on_result_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: PayloadContext for this PayloadInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadContext
        """
        if self._context is None:
            self._context = PayloadContext(
                self._version,
                account_sid=self._solution['account_sid'],
                reference_sid=self._solution['reference_sid'],
                add_on_result_sid=self._solution['add_on_result_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this payload
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def add_on_result_sid(self):
        """
        :returns: A string that uniquely identifies the result
        :rtype: unicode
        """
        return self._properties['add_on_result_sid']

    @property
    def account_sid(self):
        """
        :returns: The unique sid that identifies this account
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def label(self):
        """
        :returns: A string that describes the payload.
        :rtype: unicode
        """
        return self._properties['label']

    @property
    def add_on_sid(self):
        """
        :returns: A string that uniquely identifies the Add-on.
        :rtype: unicode
        """
        return self._properties['add_on_sid']

    @property
    def add_on_configuration_sid(self):
        """
        :returns: A string that uniquely identifies the Add-on configuration.
        :rtype: unicode
        """
        return self._properties['add_on_configuration_sid']

    @property
    def content_type(self):
        """
        :returns: The MIME type of the payload.
        :rtype: unicode
        """
        return self._properties['content_type']

    @property
    def date_created(self):
        """
        :returns: The date this resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def reference_sid(self):
        """
        :returns: A string that uniquely identifies the recording.
        :rtype: unicode
        """
        return self._properties['reference_sid']

    @property
    def subresource_uris(self):
        """
        :returns: The subresource_uris
        :rtype: unicode
        """
        return self._properties['subresource_uris']

    def fetch(self):
        """
        Fetch a PayloadInstance

        :returns: Fetched PayloadInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.payload.PayloadInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the PayloadInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.PayloadInstance {}>'.format(context)
