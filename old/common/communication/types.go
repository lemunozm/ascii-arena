package communication

import "encoding/gob"

type VersionData struct {
	Version string
}

type LogInStatus uint8

const (
	LOG_IN_STATUS_OK LogInStatus = iota
	LOG_IN_STATUS_PLAYER_ALREADY_EXISTS
	LOG_IN_STATUS_PLAYER_LIMIT_REACHED
)

type VersionCheckedData struct {
	Version    string
	Validation bool
}

type LogInData struct {
	Player        int8
	ClientUdpPort uint16
}

type LogInStatusData struct {
	LogInStatus       LogInStatus
	ServerUdpPort     uint16
	RequiredPlayers   uint32
	RegisteredPlayers []int8
}

type PlayerConnectionData struct {
	ConnectionState bool
	Player          int8
}

type MapData struct {
	Width  uint32
	Height uint32
	Data   []uint8
	Seed   uint32
}

type LoadMatchData struct {
	MillisecondsToStart uint32
	MapData             MapData
}

type FrameData struct {
	FrameId uint32
}

type PlayerActionData struct {
	FrameId uint32
	Action  uint32
}

func registerSerializationTypes() {
	gob.Register(VersionData{})
	gob.Register(VersionCheckedData{})
	gob.Register(LogInData{})
	gob.Register(LogInStatusData{})
	gob.Register(PlayerConnectionData{})
	gob.Register(MapData{})
	gob.Register(LoadMatchData{})
	gob.Register(FrameData{})
	gob.Register(PlayerActionData{})
}