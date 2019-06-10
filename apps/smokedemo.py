from phi.flow import *


size = [128]*2
smoke = world.Smoke(Domain(size, SLIPPERY))
world.Obstacle(box[60:64, 40:128-40])
world.Inflow(box[size[-2]//8, size[-1]*3//8:size[-1]*5//8])


class SmokeDemo(FieldSequenceModel):

    def __init__(self):
        FieldSequenceModel.__init__(self, 'Smoke Demo '+'x'.join([str(d) for d in size]), stride=3)
        self.state = zeros(smoke.shape())

        self.add_field('Density', lambda: self.state.density)
        self.add_field('Velocity', lambda: self.state.velocity)
        self.add_field('Pressure', lambda: smoke.last_pressure)
        self.add_field('Divergence after', lambda: divergence(self.state.velocity))
        self.add_field('Domain', lambda: smoke.domainstate.active(extend=1))

    def step(self):
        self.state = smoke.step(self.state)


app = SmokeDemo().show(display=('Density', 'Velocity'), framerate=2, production=__name__ != '__main__')