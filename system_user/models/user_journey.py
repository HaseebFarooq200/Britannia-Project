from django.db import models
from system_user.models.base_model import BaseModel


class JourneyBooking(BaseModel):
    """
    This model describes the base user of the system.

    Fields:
    1. JourneyID: PrimaryKey
    2. PickupLocation: CharField
    3. Destination: CharField
    4. IsOneWay: Boolean Field
    5. NumberOfPassengers: Integer Field
    6. NumberOfLuggages: Integer Field
    7. JourneyDate: Date Field
    8. JourneyTime: Time Field
    9. JourneyStatus: CharField
    10. CreatedAt: DateField
    11. UpdatedAt: DateField
    12. MetaStatus: CharField

    """

    JourneyID = models.AutoField(primary_key=True, db_column="journey_id")
    PickupLocation = models.CharField(max_length=128, db_column="pickup_location")
    Destination = models.CharField(max_length=128, db_column="destination")
    IsOneWay = models.BooleanField(default=True, db_column="is_one_way")
    NumberOfPassenegers = models.IntegerField(
        default=1, db_column="number_of_passengers"
    )
    NumberOfLuggages = models.IntegerField(default=0, db_column="number_of_luggages")
    JourneyDate = models.DateField(db_column="journey_date")
    JourneyTime = models.TimeField(db_column="journey_time")
    JourneyStatus = models.CharField(default="pending", db_column="journey_status")

    class Meta:
        db_table = "user_journey"
