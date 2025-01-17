from Widget import Widget
from datetime import datetime

widgets = [
    Widget('widgetV4a68520a32fd4c99a55514b35565cd3f'),
    Widget('widgetVa693557cad374256a4a2d804e3f43a89'),
    Widget('widgetVb3dd31046a93420f94f8368dc8f2450a', -1, 100),
    Widget('widgetVf74fbfd4e5104d6f839de0711c7ea8d2'),
    Widget('widgetVbc3682bf78e24760bb89d255538a6d4b'),
    Widget('widgetVe8faeb3c29d543ae964375a15ed38ca3'),
    Widget('widgetV0ec6bdc7fc6e4a9486c204c223cb67e7'),
    Widget('widgetVb2dc04786f83421090d6f1b8d6b0b4d3'),
    Widget('widgetVee0b0317c8414b5eb5258a5ebb8c2724'),
    Widget('widgetV40cdaa02fc8a471aa5ae7e3ad3020107'),
    Widget('widgetVe95f195040ad4356a11643b974119e61'),
    Widget('widgetV6bc1e8330acb4e2390a5b37082139f80'),
    Widget('widgetV7f06a09e11a44464a3c7db86165dd052'),
    Widget('widgetVd00e161176534b0e99d8e438cb38fb4e'),
    Widget('widgetVb2bd17da82444c22abf57dcd329d4158'),
    Widget('widgetV64ee6bb6e69246068b68849c5505e3d7'),
    Widget('widgetV30ec8af34ffd4ca7b02eab0ed93038bf'),
    Widget('widgetVbb2205ed4e6149eb9d5bc99fe22e1199'),
    Widget('widgetVba160ed8187e429abb7ad3b2278e5866'),
    Widget('widgetV5b41e3b2d9144bafab33475f91d689cd'),
    Widget('widgetV952fa8ef7a2a41b9bb28e5dc54250c35'),
    Widget('widgetV8206a08de25348c399996b0e79e459e8'),
    Widget('widgetVf6e84a885d4a4aa6a04a1b39d8060ce1'),
    Widget('widgetV1b1a0f5ee2654162bbb601e2411721f6'),
    Widget('widgetV3c17f158d6fd48f3bbde5542cd33bc45'),
    Widget('widgetV1bf6f9d736eb409d99bfe469d3a01686'),
    Widget('widgetVc79b449ecd0f4edb97c0f9e798f2248e'),
    Widget('widgetVf898736f3e714cd4bed4a48b692eb6f0'),
    Widget('widgetV691df9c5a4384908acbc35323408a544'),
    Widget('widgetV30cfb0b004f3436abbc7611b4028ec6c'),
    Widget('widgetVed88bd406abb4d0cb8f8fe428dc11136'),
    Widget('widgetV70c0f9b4c3b44460b4fe7d08a7204c7b'),
    Widget('widgetV3a3bd88e5cf04a1a849459235d4dde70'),
    Widget('widgetV04cef8e50be7412bb17682d3046fe531'),
    Widget('widgetVcf08d35f43ba4d978bc2e36ebc603599'),
    Widget('widgetVdb092f8518d0493ca8ba10d5df355d08'),
    Widget('widgetV71d7234bf87d4638873e1ea38bf0445f'),
    Widget('widgetVb2cc46e8c69945aa90bf2ede9c7bc04a'),
    Widget('widgetVedbdb2700c094af8a28460478f25424a'),
    Widget('widgetV0d81db7fe191421cb14c5d993d1581fe')
]

while True:
    for widget in widgets:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S") + f".{now.microsecond // 1000:03d}"
        # print(f"{widget.id} Current Time:", current_time)
            
        if widget.isValueChanged():
            widget.updateValue()
            widget.checkIfIsOverThreshold()
