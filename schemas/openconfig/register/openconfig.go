/*
Copyright 2018 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

// Package openconfig registers generated gostructs with "openconfig" key.
package openconfig

import (
	log "github.com/golang/glog"
	"github.com/openconfig/gnmitest/schemas/openconfig"
	"github.com/openconfig/gnmitest/schemas"
)

// Key is used as the key in GoStructs lookup table.
const Key = "openconfig"

func init() {
	if err := schema.Set(Key, &gostructs.Device{}, gostructs.SchemaTree, gostructs.Unmarshal); err != nil {
		log.Fatal(err)
	}
}
