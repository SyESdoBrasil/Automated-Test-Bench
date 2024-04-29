def configure_span_and_center(ena, span=10e6, center_frequency=3e6):
  """Configures the span and center frequency of the ENA display.

  Args:
      ena: The connected ENA resource object.
      span: The desired span width in Hz (default: 10 MHz).
      center_frequency: The desired center frequency in Hz (default: 3 MHz).
  """
  ena.write("SENS1:FREQ:SPAN {}".format(span))
  print(f"Set span to {span} Hz")

  ena.write(":SENS1:FREQ:CENT {}".format(center_frequency))
  print(f"Set center frequency to {center_frequency} Hz")


# ... (rest of your script)

configure_span_and_center(ena, span=20e6, center_frequency=1.5e9)