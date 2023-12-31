from kafka.admin import KafkaAdminClient, NewTopic

def delete_topics(admin):
    admin.delete_topics(topics=['games_details'])


def create_topics(admin, topic_list):
    print("Creating topics ")
    admin.create_topics(new_topics=topic_list, validate_only=False)


if __name__ == '__main__':
    admin_client = KafkaAdminClient(bootstrap_servers="35.226.94.63:9092",
                                    client_id='Assignment2')  # use your VM's external IP Here!
    topic_list = [NewTopic(name="games_details", num_partitions=1, replication_factor=1)]
    create_topics(admin_client, topic_list)
