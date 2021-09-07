- name: Install specified python requirements and custom Index URL
  pip:
    requirements: /helloansible/requirements.txt
    extra_args: -i https://github.com/Pankhuri1804/helloansible.git
