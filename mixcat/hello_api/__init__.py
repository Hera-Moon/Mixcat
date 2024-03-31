from .controller.hello import HelloController
from ..spec_base import BlueprintWithApiSpec

hello_bp = BlueprintWithApiSpec("hello", __name__)

hello_bp.add_url_rule("/hello", view_func=HelloController.as_view("hello"))
