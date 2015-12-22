FROM phusion/baseimage:0.9.17

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq && \
    apt-get install -y -qq \
    bind9

ADD configurator.py /configurator.py

EXPOSE 53

ENTRYPOINT ["/configurator.py"]
CMD ["/usr/sbin/named", "-f"]
