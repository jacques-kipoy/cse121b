# CSE 111 Class
# Week 05 L05 Prove Milestone: Testing and fixing Functions
# Jacques Kipoy
# Professor : David Christofferson

from pytest import approx
import pytest
from water_flow import water_column_height , pressure_gain_from_water_height , \
pressure_loss_from_pipe


def test_water_column_height():
    assert water_column_height(0, 0) == approx(0, abs=0.01)
    assert water_column_height(0, 10) == approx(7.5, abs=0.1)
    assert water_column_height(25, 0) == approx(25, abs=0.1)
    assert water_column_height(48.3, 12.8) == approx(57.9 , abs=0.1)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0) == approx(0, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50) == approx(489.450, abs=.001)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0, 1.75) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 0) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65) == approx(-100.4620, abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)


pytest.main(["-v", "--tb=line", "-rN", __file__])