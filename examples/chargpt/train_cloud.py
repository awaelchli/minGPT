from lightning import LightningApp, LightningWork, CloudCompute
from lightning.app.components import LiteMultiNode
from train import main


class Work(LightningWork):
    def run(self):
        main()


app = LightningApp(
    LiteMultiNode(
        Work,
        num_nodes=2,
        cloud_compute=CloudCompute(name="gpu-fast-multi"),
    )
)