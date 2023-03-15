# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class YesterdayList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the YesterdayList

        :param Version version: Version that contains the resource
        :param account_sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayList
        :rtype: twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayList
        """
        super(YesterdayList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, }
        self._uri = '/Accounts/{account_sid}/Usage/Records/Yesterday.json'.format(**self._solution)

    def stream(self, category=values.unset, start_date=values.unset,
               end_date=values.unset, include_subaccounts=values.unset, limit=None,
               page_size=None):
        """
        Streams YesterdayInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param YesterdayInstance.Category category: The usage category of the UsageRecord resources to read
        :param date start_date: Only include usage that has occurred on or after this date
        :param date end_date: Only include usage that occurred on or before this date
        :param bool include_subaccounts: Whether to include usage from the master account and all its subaccounts
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            category=category,
            start_date=start_date,
            end_date=end_date,
            include_subaccounts=include_subaccounts,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'])

    def list(self, category=values.unset, start_date=values.unset,
             end_date=values.unset, include_subaccounts=values.unset, limit=None,
             page_size=None):
        """
        Lists YesterdayInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param YesterdayInstance.Category category: The usage category of the UsageRecord resources to read
        :param date start_date: Only include usage that has occurred on or after this date
        :param date end_date: Only include usage that occurred on or before this date
        :param bool include_subaccounts: Whether to include usage from the master account and all its subaccounts
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayInstance]
        """
        return list(self.stream(
            category=category,
            start_date=start_date,
            end_date=end_date,
            include_subaccounts=include_subaccounts,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, category=values.unset, start_date=values.unset,
             end_date=values.unset, include_subaccounts=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of YesterdayInstance records from the API.
        Request is executed immediately

        :param YesterdayInstance.Category category: The usage category of the UsageRecord resources to read
        :param date start_date: Only include usage that has occurred on or after this date
        :param date end_date: Only include usage that occurred on or before this date
        :param bool include_subaccounts: Whether to include usage from the master account and all its subaccounts
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of YesterdayInstance
        :rtype: twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayPage
        """
        data = values.of({
            'Category': category,
            'StartDate': serialize.iso8601_date(start_date),
            'EndDate': serialize.iso8601_date(end_date),
            'IncludeSubaccounts': include_subaccounts,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return YesterdayPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of YesterdayInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of YesterdayInstance
        :rtype: twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return YesterdayPage(self._version, response, self._solution)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.YesterdayList>'


class YesterdayPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the YesterdayPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayPage
        :rtype: twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayPage
        """
        super(YesterdayPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of YesterdayInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayInstance
        :rtype: twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayInstance
        """
        return YesterdayInstance(self._version, payload, account_sid=self._solution['account_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.YesterdayPage>'


class YesterdayInstance(InstanceResource):

    class Category(object):
        A2P_REGISTRATION_FEES = "a2p-registration-fees"
        AGENT_CONFERENCE = "agent-conference"
        AMAZON_POLLY = "amazon-polly"
        ANSWERING_MACHINE_DETECTION = "answering-machine-detection"
        AUTHY_AUTHENTICATIONS = "authy-authentications"
        AUTHY_CALLS_OUTBOUND = "authy-calls-outbound"
        AUTHY_MONTHLY_FEES = "authy-monthly-fees"
        AUTHY_PHONE_INTELLIGENCE = "authy-phone-intelligence"
        AUTHY_PHONE_VERIFICATIONS = "authy-phone-verifications"
        AUTHY_SMS_OUTBOUND = "authy-sms-outbound"
        CALL_PROGESS_EVENTS = "call-progess-events"
        CALLERIDLOOKUPS = "calleridlookups"
        CALLS = "calls"
        CALLS_CLIENT = "calls-client"
        CALLS_GLOBALCONFERENCE = "calls-globalconference"
        CALLS_INBOUND = "calls-inbound"
        CALLS_INBOUND_LOCAL = "calls-inbound-local"
        CALLS_INBOUND_MOBILE = "calls-inbound-mobile"
        CALLS_INBOUND_TOLLFREE = "calls-inbound-tollfree"
        CALLS_OUTBOUND = "calls-outbound"
        CALLS_PAY_VERB_TRANSACTIONS = "calls-pay-verb-transactions"
        CALLS_RECORDINGS = "calls-recordings"
        CALLS_SIP = "calls-sip"
        CALLS_SIP_INBOUND = "calls-sip-inbound"
        CALLS_SIP_OUTBOUND = "calls-sip-outbound"
        CALLS_TRANSFERS = "calls-transfers"
        CARRIER_LOOKUPS = "carrier-lookups"
        CONVERSATIONS = "conversations"
        CONVERSATIONS_API_REQUESTS = "conversations-api-requests"
        CONVERSATIONS_CONVERSATION_EVENTS = "conversations-conversation-events"
        CONVERSATIONS_ENDPOINT_CONNECTIVITY = "conversations-endpoint-connectivity"
        CONVERSATIONS_EVENTS = "conversations-events"
        CONVERSATIONS_PARTICIPANT_EVENTS = "conversations-participant-events"
        CONVERSATIONS_PARTICIPANTS = "conversations-participants"
        CPS = "cps"
        FLEX_USAGE = "flex-usage"
        FRAUD_LOOKUPS = "fraud-lookups"
        GROUP_ROOMS = "group-rooms"
        GROUP_ROOMS_DATA_TRACK = "group-rooms-data-track"
        GROUP_ROOMS_ENCRYPTED_MEDIA_RECORDED = "group-rooms-encrypted-media-recorded"
        GROUP_ROOMS_MEDIA_DOWNLOADED = "group-rooms-media-downloaded"
        GROUP_ROOMS_MEDIA_RECORDED = "group-rooms-media-recorded"
        GROUP_ROOMS_MEDIA_ROUTED = "group-rooms-media-routed"
        GROUP_ROOMS_MEDIA_STORED = "group-rooms-media-stored"
        GROUP_ROOMS_PARTICIPANT_MINUTES = "group-rooms-participant-minutes"
        GROUP_ROOMS_RECORDED_MINUTES = "group-rooms-recorded-minutes"
        IMP_V1_USAGE = "imp-v1-usage"
        LOOKUPS = "lookups"
        MARKETPLACE = "marketplace"
        MARKETPLACE_ALGORITHMIA_NAMED_ENTITY_RECOGNITION = "marketplace-algorithmia-named-entity-recognition"
        MARKETPLACE_CADENCE_TRANSCRIPTION = "marketplace-cadence-transcription"
        MARKETPLACE_CADENCE_TRANSLATION = "marketplace-cadence-translation"
        MARKETPLACE_CAPIO_SPEECH_TO_TEXT = "marketplace-capio-speech-to-text"
        MARKETPLACE_CONVRIZA_ABABA = "marketplace-convriza-ababa"
        MARKETPLACE_DEEPGRAM_PHRASE_DETECTOR = "marketplace-deepgram-phrase-detector"
        MARKETPLACE_DIGITAL_SEGMENT_BUSINESS_INFO = "marketplace-digital-segment-business-info"
        MARKETPLACE_FACEBOOK_OFFLINE_CONVERSIONS = "marketplace-facebook-offline-conversions"
        MARKETPLACE_GOOGLE_SPEECH_TO_TEXT = "marketplace-google-speech-to-text"
        MARKETPLACE_IBM_WATSON_MESSAGE_INSIGHTS = "marketplace-ibm-watson-message-insights"
        MARKETPLACE_IBM_WATSON_MESSAGE_SENTIMENT = "marketplace-ibm-watson-message-sentiment"
        MARKETPLACE_IBM_WATSON_RECORDING_ANALYSIS = "marketplace-ibm-watson-recording-analysis"
        MARKETPLACE_IBM_WATSON_TONE_ANALYZER = "marketplace-ibm-watson-tone-analyzer"
        MARKETPLACE_ICEHOOK_SYSTEMS_SCOUT = "marketplace-icehook-systems-scout"
        MARKETPLACE_INFOGROUP_DATAAXLE_BIZINFO = "marketplace-infogroup-dataaxle-bizinfo"
        MARKETPLACE_KEEN_IO_CONTACT_CENTER_ANALYTICS = "marketplace-keen-io-contact-center-analytics"
        MARKETPLACE_MARCHEX_CLEANCALL = "marketplace-marchex-cleancall"
        MARKETPLACE_MARCHEX_SENTIMENT_ANALYSIS_FOR_SMS = "marketplace-marchex-sentiment-analysis-for-sms"
        MARKETPLACE_MARKETPLACE_NEXTCALLER_SOCIAL_ID = "marketplace-marketplace-nextcaller-social-id"
        MARKETPLACE_MOBILE_COMMONS_OPT_OUT_CLASSIFIER = "marketplace-mobile-commons-opt-out-classifier"
        MARKETPLACE_NEXIWAVE_VOICEMAIL_TO_TEXT = "marketplace-nexiwave-voicemail-to-text"
        MARKETPLACE_NEXTCALLER_ADVANCED_CALLER_IDENTIFICATION = "marketplace-nextcaller-advanced-caller-identification"
        MARKETPLACE_NOMOROBO_SPAM_SCORE = "marketplace-nomorobo-spam-score"
        MARKETPLACE_PAYFONE_TCPA_COMPLIANCE = "marketplace-payfone-tcpa-compliance"
        MARKETPLACE_REMEETING_AUTOMATIC_SPEECH_RECOGNITION = "marketplace-remeeting-automatic-speech-recognition"
        MARKETPLACE_TCPA_DEFENSE_SOLUTIONS_BLACKLIST_FEED = "marketplace-tcpa-defense-solutions-blacklist-feed"
        MARKETPLACE_TELO_OPENCNAM = "marketplace-telo-opencnam"
        MARKETPLACE_TRUECNAM_TRUE_SPAM = "marketplace-truecnam-true-spam"
        MARKETPLACE_TWILIO_CALLER_NAME_LOOKUP_US = "marketplace-twilio-caller-name-lookup-us"
        MARKETPLACE_TWILIO_CARRIER_INFORMATION_LOOKUP = "marketplace-twilio-carrier-information-lookup"
        MARKETPLACE_VOICEBASE_PCI = "marketplace-voicebase-pci"
        MARKETPLACE_VOICEBASE_TRANSCRIPTION = "marketplace-voicebase-transcription"
        MARKETPLACE_VOICEBASE_TRANSCRIPTION_CUSTOM_VOCABULARY = "marketplace-voicebase-transcription-custom-vocabulary"
        MARKETPLACE_WHITEPAGES_PRO_CALLER_IDENTIFICATION = "marketplace-whitepages-pro-caller-identification"
        MARKETPLACE_WHITEPAGES_PRO_PHONE_INTELLIGENCE = "marketplace-whitepages-pro-phone-intelligence"
        MARKETPLACE_WHITEPAGES_PRO_PHONE_REPUTATION = "marketplace-whitepages-pro-phone-reputation"
        MARKETPLACE_WOLFARM_SPOKEN_RESULTS = "marketplace-wolfarm-spoken-results"
        MARKETPLACE_WOLFRAM_SHORT_ANSWER = "marketplace-wolfram-short-answer"
        MARKETPLACE_YTICA_CONTACT_CENTER_REPORTING_ANALYTICS = "marketplace-ytica-contact-center-reporting-analytics"
        MEDIASTORAGE = "mediastorage"
        MMS = "mms"
        MMS_INBOUND = "mms-inbound"
        MMS_INBOUND_LONGCODE = "mms-inbound-longcode"
        MMS_INBOUND_SHORTCODE = "mms-inbound-shortcode"
        MMS_MESSAGES_CARRIERFEES = "mms-messages-carrierfees"
        MMS_OUTBOUND = "mms-outbound"
        MMS_OUTBOUND_LONGCODE = "mms-outbound-longcode"
        MMS_OUTBOUND_SHORTCODE = "mms-outbound-shortcode"
        MONITOR_READS = "monitor-reads"
        MONITOR_STORAGE = "monitor-storage"
        MONITOR_WRITES = "monitor-writes"
        NOTIFY = "notify"
        NOTIFY_ACTIONS_ATTEMPTS = "notify-actions-attempts"
        NOTIFY_CHANNELS = "notify-channels"
        NUMBER_FORMAT_LOOKUPS = "number-format-lookups"
        PCHAT = "pchat"
        PCHAT_USERS = "pchat-users"
        PEER_TO_PEER_ROOMS_PARTICIPANT_MINUTES = "peer-to-peer-rooms-participant-minutes"
        PFAX = "pfax"
        PFAX_MINUTES = "pfax-minutes"
        PFAX_MINUTES_INBOUND = "pfax-minutes-inbound"
        PFAX_MINUTES_OUTBOUND = "pfax-minutes-outbound"
        PFAX_PAGES = "pfax-pages"
        PHONENUMBERS = "phonenumbers"
        PHONENUMBERS_CPS = "phonenumbers-cps"
        PHONENUMBERS_EMERGENCY = "phonenumbers-emergency"
        PHONENUMBERS_LOCAL = "phonenumbers-local"
        PHONENUMBERS_MOBILE = "phonenumbers-mobile"
        PHONENUMBERS_SETUPS = "phonenumbers-setups"
        PHONENUMBERS_TOLLFREE = "phonenumbers-tollfree"
        PREMIUMSUPPORT = "premiumsupport"
        PROXY = "proxy"
        PROXY_ACTIVE_SESSIONS = "proxy-active-sessions"
        PSTNCONNECTIVITY = "pstnconnectivity"
        PV = "pv"
        PV_COMPOSITION_MEDIA_DOWNLOADED = "pv-composition-media-downloaded"
        PV_COMPOSITION_MEDIA_ENCRYPTED = "pv-composition-media-encrypted"
        PV_COMPOSITION_MEDIA_STORED = "pv-composition-media-stored"
        PV_COMPOSITION_MINUTES = "pv-composition-minutes"
        PV_RECORDING_COMPOSITIONS = "pv-recording-compositions"
        PV_ROOM_PARTICIPANTS = "pv-room-participants"
        PV_ROOM_PARTICIPANTS_AU1 = "pv-room-participants-au1"
        PV_ROOM_PARTICIPANTS_BR1 = "pv-room-participants-br1"
        PV_ROOM_PARTICIPANTS_IE1 = "pv-room-participants-ie1"
        PV_ROOM_PARTICIPANTS_JP1 = "pv-room-participants-jp1"
        PV_ROOM_PARTICIPANTS_SG1 = "pv-room-participants-sg1"
        PV_ROOM_PARTICIPANTS_US1 = "pv-room-participants-us1"
        PV_ROOM_PARTICIPANTS_US2 = "pv-room-participants-us2"
        PV_ROOMS = "pv-rooms"
        PV_SIP_ENDPOINT_REGISTRATIONS = "pv-sip-endpoint-registrations"
        RECORDINGS = "recordings"
        RECORDINGSTORAGE = "recordingstorage"
        ROOMS_GROUP_BANDWIDTH = "rooms-group-bandwidth"
        ROOMS_GROUP_MINUTES = "rooms-group-minutes"
        ROOMS_PEER_TO_PEER_MINUTES = "rooms-peer-to-peer-minutes"
        SHORTCODES = "shortcodes"
        SHORTCODES_CUSTOMEROWNED = "shortcodes-customerowned"
        SHORTCODES_MMS_ENABLEMENT = "shortcodes-mms-enablement"
        SHORTCODES_MPS = "shortcodes-mps"
        SHORTCODES_RANDOM = "shortcodes-random"
        SHORTCODES_UK = "shortcodes-uk"
        SHORTCODES_VANITY = "shortcodes-vanity"
        SMALL_GROUP_ROOMS = "small-group-rooms"
        SMALL_GROUP_ROOMS_DATA_TRACK = "small-group-rooms-data-track"
        SMALL_GROUP_ROOMS_PARTICIPANT_MINUTES = "small-group-rooms-participant-minutes"
        SMS = "sms"
        SMS_INBOUND = "sms-inbound"
        SMS_INBOUND_LONGCODE = "sms-inbound-longcode"
        SMS_INBOUND_SHORTCODE = "sms-inbound-shortcode"
        SMS_MESSAGES_CARRIERFEES = "sms-messages-carrierfees"
        SMS_MESSAGES_FEATURES = "sms-messages-features"
        SMS_MESSAGES_FEATURES_SENDERID = "sms-messages-features-senderid"
        SMS_OUTBOUND = "sms-outbound"
        SMS_OUTBOUND_CONTENT_INSPECTION = "sms-outbound-content-inspection"
        SMS_OUTBOUND_LONGCODE = "sms-outbound-longcode"
        SMS_OUTBOUND_SHORTCODE = "sms-outbound-shortcode"
        SPEECH_RECOGNITION = "speech-recognition"
        STUDIO_ENGAGEMENTS = "studio-engagements"
        SYNC = "sync"
        SYNC_ACTIONS = "sync-actions"
        SYNC_ENDPOINT_HOURS = "sync-endpoint-hours"
        SYNC_ENDPOINT_HOURS_ABOVE_DAILY_CAP = "sync-endpoint-hours-above-daily-cap"
        TASKROUTER_TASKS = "taskrouter-tasks"
        TOTALPRICE = "totalprice"
        TRANSCRIPTIONS = "transcriptions"
        TRUNKING_CPS = "trunking-cps"
        TRUNKING_EMERGENCY_CALLS = "trunking-emergency-calls"
        TRUNKING_ORIGINATION = "trunking-origination"
        TRUNKING_ORIGINATION_LOCAL = "trunking-origination-local"
        TRUNKING_ORIGINATION_MOBILE = "trunking-origination-mobile"
        TRUNKING_ORIGINATION_TOLLFREE = "trunking-origination-tollfree"
        TRUNKING_RECORDINGS = "trunking-recordings"
        TRUNKING_SECURE = "trunking-secure"
        TRUNKING_TERMINATION = "trunking-termination"
        TURNMEGABYTES = "turnmegabytes"
        TURNMEGABYTES_AUSTRALIA = "turnmegabytes-australia"
        TURNMEGABYTES_BRASIL = "turnmegabytes-brasil"
        TURNMEGABYTES_GERMANY = "turnmegabytes-germany"
        TURNMEGABYTES_INDIA = "turnmegabytes-india"
        TURNMEGABYTES_IRELAND = "turnmegabytes-ireland"
        TURNMEGABYTES_JAPAN = "turnmegabytes-japan"
        TURNMEGABYTES_SINGAPORE = "turnmegabytes-singapore"
        TURNMEGABYTES_USEAST = "turnmegabytes-useast"
        TURNMEGABYTES_USWEST = "turnmegabytes-uswest"
        TWILIO_INTERCONNECT = "twilio-interconnect"
        VERIFY_PUSH = "verify-push"
        VERIFY_TOTP = "verify-totp"
        VERIFY_WHATSAPP_CONVERSATIONS_BUSINESS_INITIATED = "verify-whatsapp-conversations-business-initiated"
        VIDEO_RECORDINGS = "video-recordings"
        VIRTUAL_AGENT = "virtual-agent"
        VOICE_INSIGHTS = "voice-insights"
        VOICE_INSIGHTS_CLIENT_INSIGHTS_ON_DEMAND_MINUTE = "voice-insights-client-insights-on-demand-minute"
        VOICE_INSIGHTS_PTSN_INSIGHTS_ON_DEMAND_MINUTE = "voice-insights-ptsn-insights-on-demand-minute"
        VOICE_INSIGHTS_SIP_INTERFACE_INSIGHTS_ON_DEMAND_MINUTE = "voice-insights-sip-interface-insights-on-demand-minute"
        VOICE_INSIGHTS_SIP_TRUNKING_INSIGHTS_ON_DEMAND_MINUTE = "voice-insights-sip-trunking-insights-on-demand-minute"
        WIRELESS = "wireless"
        WIRELESS_ORDERS = "wireless-orders"
        WIRELESS_ORDERS_ARTWORK = "wireless-orders-artwork"
        WIRELESS_ORDERS_BULK = "wireless-orders-bulk"
        WIRELESS_ORDERS_ESIM = "wireless-orders-esim"
        WIRELESS_ORDERS_STARTER = "wireless-orders-starter"
        WIRELESS_USAGE = "wireless-usage"
        WIRELESS_USAGE_COMMANDS = "wireless-usage-commands"
        WIRELESS_USAGE_COMMANDS_AFRICA = "wireless-usage-commands-africa"
        WIRELESS_USAGE_COMMANDS_ASIA = "wireless-usage-commands-asia"
        WIRELESS_USAGE_COMMANDS_CENTRALANDSOUTHAMERICA = "wireless-usage-commands-centralandsouthamerica"
        WIRELESS_USAGE_COMMANDS_EUROPE = "wireless-usage-commands-europe"
        WIRELESS_USAGE_COMMANDS_HOME = "wireless-usage-commands-home"
        WIRELESS_USAGE_COMMANDS_NORTHAMERICA = "wireless-usage-commands-northamerica"
        WIRELESS_USAGE_COMMANDS_OCEANIA = "wireless-usage-commands-oceania"
        WIRELESS_USAGE_COMMANDS_ROAMING = "wireless-usage-commands-roaming"
        WIRELESS_USAGE_DATA = "wireless-usage-data"
        WIRELESS_USAGE_DATA_AFRICA = "wireless-usage-data-africa"
        WIRELESS_USAGE_DATA_ASIA = "wireless-usage-data-asia"
        WIRELESS_USAGE_DATA_CENTRALANDSOUTHAMERICA = "wireless-usage-data-centralandsouthamerica"
        WIRELESS_USAGE_DATA_CUSTOM_ADDITIONALMB = "wireless-usage-data-custom-additionalmb"
        WIRELESS_USAGE_DATA_CUSTOM_FIRST5MB = "wireless-usage-data-custom-first5mb"
        WIRELESS_USAGE_DATA_DOMESTIC_ROAMING = "wireless-usage-data-domestic-roaming"
        WIRELESS_USAGE_DATA_EUROPE = "wireless-usage-data-europe"
        WIRELESS_USAGE_DATA_INDIVIDUAL_ADDITIONALGB = "wireless-usage-data-individual-additionalgb"
        WIRELESS_USAGE_DATA_INDIVIDUAL_FIRSTGB = "wireless-usage-data-individual-firstgb"
        WIRELESS_USAGE_DATA_INTERNATIONAL_ROAMING_CANADA = "wireless-usage-data-international-roaming-canada"
        WIRELESS_USAGE_DATA_INTERNATIONAL_ROAMING_INDIA = "wireless-usage-data-international-roaming-india"
        WIRELESS_USAGE_DATA_INTERNATIONAL_ROAMING_MEXICO = "wireless-usage-data-international-roaming-mexico"
        WIRELESS_USAGE_DATA_NORTHAMERICA = "wireless-usage-data-northamerica"
        WIRELESS_USAGE_DATA_OCEANIA = "wireless-usage-data-oceania"
        WIRELESS_USAGE_DATA_POOLED = "wireless-usage-data-pooled"
        WIRELESS_USAGE_DATA_POOLED_DOWNLINK = "wireless-usage-data-pooled-downlink"
        WIRELESS_USAGE_DATA_POOLED_UPLINK = "wireless-usage-data-pooled-uplink"
        WIRELESS_USAGE_MRC = "wireless-usage-mrc"
        WIRELESS_USAGE_MRC_CUSTOM = "wireless-usage-mrc-custom"
        WIRELESS_USAGE_MRC_INDIVIDUAL = "wireless-usage-mrc-individual"
        WIRELESS_USAGE_MRC_POOLED = "wireless-usage-mrc-pooled"
        WIRELESS_USAGE_MRC_SUSPENDED = "wireless-usage-mrc-suspended"
        WIRELESS_USAGE_SMS = "wireless-usage-sms"
        WIRELESS_USAGE_VOICE = "wireless-usage-voice"

    def __init__(self, version, payload, account_sid):
        """
        Initialize the YesterdayInstance

        :returns: twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayInstance
        :rtype: twilio.rest.api.v2010.account.usage.record.yesterday.YesterdayInstance
        """
        super(YesterdayInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'api_version': payload.get('api_version'),
            'as_of': payload.get('as_of'),
            'category': payload.get('category'),
            'count': payload.get('count'),
            'count_unit': payload.get('count_unit'),
            'description': payload.get('description'),
            'end_date': deserialize.iso8601_date(payload.get('end_date')),
            'price': deserialize.decimal(payload.get('price')),
            'price_unit': payload.get('price_unit'),
            'start_date': deserialize.iso8601_date(payload.get('start_date')),
            'subresource_uris': payload.get('subresource_uris'),
            'uri': payload.get('uri'),
            'usage': payload.get('usage'),
            'usage_unit': payload.get('usage_unit'),
        }

        # Context
        self._context = None
        self._solution = {'account_sid': account_sid, }

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account accrued the usage
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def api_version(self):
        """
        :returns: The API version used to create the resource
        :rtype: unicode
        """
        return self._properties['api_version']

    @property
    def as_of(self):
        """
        :returns: Usage records up to date as of this timestamp
        :rtype: unicode
        """
        return self._properties['as_of']

    @property
    def category(self):
        """
        :returns: The category of usage
        :rtype: YesterdayInstance.Category
        """
        return self._properties['category']

    @property
    def count(self):
        """
        :returns: The number of usage events
        :rtype: unicode
        """
        return self._properties['count']

    @property
    def count_unit(self):
        """
        :returns: The units in which count is measured
        :rtype: unicode
        """
        return self._properties['count_unit']

    @property
    def description(self):
        """
        :returns: A plain-language description of the usage category
        :rtype: unicode
        """
        return self._properties['description']

    @property
    def end_date(self):
        """
        :returns: The last date for which usage is included in the UsageRecord
        :rtype: date
        """
        return self._properties['end_date']

    @property
    def price(self):
        """
        :returns: The total price of the usage
        :rtype: unicode
        """
        return self._properties['price']

    @property
    def price_unit(self):
        """
        :returns: The currency in which `price` is measured
        :rtype: unicode
        """
        return self._properties['price_unit']

    @property
    def start_date(self):
        """
        :returns: The first date for which usage is included in this UsageRecord
        :rtype: date
        """
        return self._properties['start_date']

    @property
    def subresource_uris(self):
        """
        :returns: A list of related resources identified by their relative URIs
        :rtype: unicode
        """
        return self._properties['subresource_uris']

    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`
        :rtype: unicode
        """
        return self._properties['uri']

    @property
    def usage(self):
        """
        :returns: The amount of usage
        :rtype: unicode
        """
        return self._properties['usage']

    @property
    def usage_unit(self):
        """
        :returns: The units in which usage is measured
        :rtype: unicode
        """
        return self._properties['usage_unit']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.YesterdayInstance>'
